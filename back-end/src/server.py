#!flask/bin/python
import flask
from flask import Flask, jsonify, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

import json
import random

from datetime import datetime, timedelta,time


from hashlib import md5
from datetime import datetime
from functools import wraps
from db_model.db import db
from db_model.vol import *
from db_model.airport import Airport
from db_model.airport_reader import airport_reader
from db_model.admin_constante_hyst   import AdminCsteHyst
from db_model.flightcompany   import FlightCompany
from db_model.fc_reader import fc_reader
from db_model.cap_pool import CapPool
from db_model.cap_pool_reader import cap_pool_reader
from db_model.cap_horaire import CapHoraire
from db_model.cap_horaire_reader import cap_horaire_reader
from db_model.group import Group
from db_model.group_reader import group_reader
from db_model.user import User
from db_model.admin import Admin
from db_model.regles_aff import RegleAff
from db_model.regle_aff_reader import regle_aff_reader
from db_model.user import populateUser
from db_model.nav import Nav
from db_model.priorite import Priorite
from db_model.priorite_reader import priorite_reader
from db_model.contingence import Contingence
from db_model.user_fc import User_Fc
from db_model.att_conf import AttributionConfirme
from settings import postUrl
from db_model.att_prel import AttributionPreliminaire
import subprocess

app = Flask(__name__)
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = postUrl
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

CORS(app)


# TODO with postgresql
h = md5()
h.update(b'user123')
h.hexdigest()
u = User("default", h.hexdigest(), "user@gmail.com")
userlist = [u]
print(u in userlist)

@login_manager.user_loader
def load_user(id):
    return User.query.get(ord(id))

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/assets', methods=['GET'])
def get_assets():
    return "no assets"

@app.route('/init_db', methods=['GET'])
def init_db():
    db.reflect()
    db.drop_all()
    db.create_all()
    return redirect(url_for('index'))


@app.route('/populate', methods=['GET'])
def populate():
    init_db()

    # populate all tables
    result = vol_reader("../data/vols.csv")
    print(result)
    for line in result:
        vol = Vol(line['date'], line['heure'], line['noVol'], line['noVol'][:2], line['aeronef'], line['od'], line['secteur'], line['status'])
        db.session.add(vol)
    db.session.commit()

    result = airport_reader("../data/airports.csv")
    for line in result:
        airport = Airport(line['city'] , line['airportCode'],line['level2'],line['level3'])
        db.session.add(airport)
    db.session.commit()

    result = fc_reader("../data/fc.csv")
    for line in result:
        fc = FlightCompany( line['fc'])
        db.session.add(fc)
    db.session.commit()

    result = cap_pool_reader("../data/cap_pool.csv")
    for line in result:
        cap_pool = CapPool(line['cap_pool_name'])
        db.session.add(cap_pool)
    db.session.commit()

    result = cap_horaire_reader("../data/cap_horaire.csv")
    for line in result:
        cap_horaire = CapHoraire(line['cap_value'], line['cap_timestamp'], line['user_id'])
        db.session.add(cap_horaire)
    db.session.commit()

    result = group_reader("../data/group.csv")
    for line in result:
        priority_group = Group( line['fc_code'], line['group_name'],line['group_type'], line['group_class'])
        db.session.add(priority_group)
    db.session.commit()

    result = regle_aff_reader("../data/tbl_algo_regles_affaire.csv")
    for line in result:
        regle_aff = RegleAff(line['drag_capacity_from'], line['drag_capacity_to'], line['drag_type'], line['drag_value'],line['propagation'], line['condition_type'], line['condition_value'])
        db.session.add(regle_aff)
    db.session.commit()

    result = populateUser("../data/users.csv")
    for line in result:
        user = User(line['username'], line['password'], line['email'])
        print(line['isAdmin'])
        db.session.add(user)
        if (line['isAdmin'].lower() == 'true'):
            db.session.commit()
            user = User.query.filter_by(username=line['username']).first()
            admin = Admin(user.id)
            db.session.add(admin)
        if (line['isNav'].lower() == 'true'):
            db.session.commit()
            user = User.query.filter_by(username=line['username']).first()
            nav = Nav(user.id)
            db.session.add(nav)
        if (line['fc'] != ''):
            db.session.commit()
            user = User.query.filter_by(username=line['username']).first()
            nav = User_Fc(user.id, line['fc'])
            db.session.add(nav)

    db.session.commit()

    result = priorite_reader("../data/priorite.csv")
    for line in result:
        print(line)
        priorite = Priorite(line['fc_code'], line['group_id'], line['rank'])
        db.session.add(priorite)
        print(priorite)
    db.session.commit()


    return redirect(url_for('index'))

@app.route('/flights', methods=['GET'])
def flights():
    data = {'flights':[]};
    vols = Vol.query.filter_by(date='Mardi').all()
    for vol in vols:
        data['flights'].append({'time':vol.heure.__format__("%H:%M:%S"), 'flightNumber':vol.noVol, 'destination':vol.od})

    return jsonify(data)

def get_user():
    if 'Api_Access_Token' not in request.headers or 'Api_Username' not in request.headers:
        return return_error()
    else:
        token = request.headers['Api_Access_Token']
        username = request.headers['Api_Username']
        print(token)
        print(username)
        user = User.query.filter_by(username=username).filter_by(access_token=token).first()
        if user is not None:
            return user.username
        else:
            print("Error")
            return False
    return None

@app.route('/alert', methods=['GET', 'POST'])
def alert():
    #user = get_user()
    if request.method == 'GET':
        capHoraires = CapHoraire.query.filter(CapHoraire.cap_timestamp < (datetime.now() + timedelta(days=1))).filter((CapHoraire.cap_timestamp > datetime.now())).all()
        data = {'alert' : []}
        for capHoraire in capHoraires:
            vols = Vol.query.filter_by(date='Mardi').filter(Vol.heure < (capHoraire.cap_timestamp + timedelta(hours=1)).__format__("%H:%M:%S")).filter(Vol.heure >= (capHoraire.cap_timestamp).__format__("%H:%M:%S")).all()
            data['alert'].append({'cap_value':capHoraire.cap_value, 'cap_timestamp':capHoraire.cap_timestamp, 'demand': len(vols)})
        return jsonify(data)
    elif request.method == 'POST':
        print('POST')
        for key in request.args:
            print(key)
        timestamp_alert = request.form['alert']
        Contingence.query.delete()
        contin = Contingence(datetime.strptime(timestamp_alert, "%a, %d %b %Y %H:%M:%S GMT"))
        db.session.add(contin)
        db.session.commit()
        subprocess.call("Rscript.exe routing/routing_algo_r.r", shell=True)

        return jsonify({'data':'ok'})


@app.route('/rules', methods=['GET', 'POST'])
def rules():
    #user = get_user()
    if request.method == 'GET':
        rules = RegleAff.query.order_by(RegleAff.id).all()
        data = {'rules' : []}
        for rule in rules:
            data['rules'].append({'id':rule.id,
                                    'drag_capacity_from':rule.drag_capacity_from,
                                    'drag_capacity_to':rule.drag_capacity_to,
                                    'drag_type':rule.drag_type,
                                    'drag_value':rule.drag_value,
                                    'propagation':rule.propagation,
                                    'condition_type':rule.condition_type,
                                    'condition_value':rule.condition_value,})
        return jsonify(data)
    elif request.method == 'POST':
        print('POST')
        for key in request.args:
            print(key)
        rules = json.loads(request.form['rules'])
        RegleAff.query.delete()
        for rule in rules:
            print(rule)
            regle = RegleAff(rule['drag_capacity_from'],
                rule['drag_capacity_to'],
                rule['drag_type'],
                rule['drag_value'],
                rule['propagation'],
                rule['condition_type'],
                rule['condition_value'])
            db.session.add(regle)
        db.session.commit()

        return jsonify({'data':'ok'})

@app.route('/assign', methods=['GET', 'POST'])
def assign():
    user = get_user()
    if request.method == 'GET':
        user = User.query.filter_by(username=user).first()
        user_fc_relation = User_Fc.query.filter_by(user_id=user.id).first()
        atts = AttributionPreliminaire.query.filter_by(fc_code=user_fc_relation.fc).all()
        i = 0
        for att in atts:
            i += att.capacity

        timestamp_begin = Contingence.query.first().timestamp_start.__format__("%H:%M:%S");
        timestamp_end = Contingence.query.first().timestamp_end.__format__("%H:%M:%S");

        vols = Vol.query.filter_by(date='Mardi').filter(Vol.heure < timestamp_end).filter(Vol.heure > timestamp_begin).filter_by(fc=user_fc_relation.fc).all()
        noVols = [];
        for vol in vols:
            noVols.append({'value': vol.noVol, 'label': vol.noVol})

        data = {'flightCount':i, 'flights': noVols}
        return jsonify(data)
    elif request.method == 'POST':
        print('POST')
        for key in request.args:
            print(key)
        acceptedFlights = list(set(json.loads(request.form['values'])))

        if '' in acceptedFlights:
            acceptedFlights.remove('')
        print(acceptedFlights)
        # TODO remove accepted from att_prel
        # TODO add accepted to att_conf
        for flight in acceptedFlights:
            #Vol.query
        #AttributionPreliminaire.query.filter(AttributionPreliminaire.)
            print(flight)
            x=  AttributionConfirme(flight, flight[:2])
            db.session.add(x)
        db.session.commit()

        return jsonify({'data':'ok'})

@app.route('/capacity', methods=['GET', 'POST'])
def capacity():
    user = get_user()
    if request.method == 'GET':
        capHoraires = CapHoraire.query.filter(CapHoraire.cap_timestamp < datetime.now() + timedelta(days=1)).filter(CapHoraire.cap_timestamp > datetime.now())
        print(capHoraires)
        data = {'capacity' : []}
        for capHoraire in capHoraires:
            data['capacity'].append({'cap_value':capHoraire.cap_value, 'cap_timestamp':capHoraire.cap_timestamp, 'user_id':capHoraire.user_id})
        return jsonify(data)
    elif request.method == 'POST':
        print('POST')
        for key in request.args:
            print(key)
        print(request.form['json'])
        data = json.loads(request.form['json'])
        CapHoraire.query.delete()
        db.session.commit()
        for cap in data['capacity']:
            cap = CapHoraire(int(cap['cap_value']), cap['cap_timestamp'], cap['user_id'])
            db.session.add(cap)
        db.session.commit()
        return jsonify({'data':'ok'})



@app.route('/FlightCompany', methods=['GET'])
def get_flightCompany():
    return Vol.query.filter_by(fc).distinct()
    #User.query.filter_by(username='peter').first()

@app.route('/search/<searchText>', methods=['GET'])
def get_searchTitles(searchText):
    return "assets search :" + str(searchText)

@app.route('/register' , methods=['POST'])
def register():
    user = User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    # TODO add an email confirmation
    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print("login process")
    registered_user = User.query.filter_by(username=username).filter_by(password=password).first()
    if registered_user is None:
        print('Username or Password is invalid')
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))

    token = int(random.random() * 2000) + 1;
    registered_user.access_token = token
    db.session.commit()

    login_user(registered_user)

    isAdminQuery = Admin.query.filter_by(user_id=registered_user.id).first()
    isAdmin = False
    if isAdminQuery != None:
        isAdmin = True

    isNavQuery = Nav.query.filter_by(user_id=registered_user.id).first()
    isNav = False
    if isNavQuery != None:
        isNav = True

    return jsonify({'auth':'ok','token': registered_user.access_token,'username': registered_user.username, 'isAdmin':isAdmin, 'isNav':isNav})

def return_error():
    return jsonify({'error': 'you do not have access'})



@app.route("/userLogged")
def userLogged(user=None):
    return user.username

@app.route("/logout")
@login_required
def logout():
    user = get_user()
    registered_user = User.query.filter_by(username=user).first()
    registered_user.access_token = 0
    db.session.commit()
    logout_user()
    return ""

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8932)
