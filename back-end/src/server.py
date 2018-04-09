#!flask/bin/python
import flask
from flask import Flask, jsonify, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required, login_user, logout_user, current_user


from hashlib import md5
from datetime import datetime
from functools import wraps
from db_model.db import db
from db_model.vol import Vol
from db_model.airport import Airport
from db_model.admin_constante_hyst   import AdminCsteHyst
from db_model.flightcompany   import FlightCompany
from db_model.cap_pool import CapPool
from db_model.cap_horaire import CapHoraire
from db_model.group import Group
from db_model.user import User
from csvreader import csvreader

app = Flask(__name__)
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
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
    #drop
    db.create_all()


@app.route('/populate', methods=['GET'])
def populate():
    init_db()
    return redirect(url_for('index'))
    # populate all tables
    for line in result:
        vol = Vol(line['date'], line['heure'], line['noVol'], line['fc'], line['aeronef'], line['od'], line['secteur'])
        db.session.add(vol)
        db.session.commit()

    for line in result:
        airport = Airport(line['city'] , line['airportCode'],line['level2'],line['level3'])
        db.session.add(airport)
        db.session.commit()
        result = csvreader("fc.csv")

    for line in result:
        fc = FlightCompany(line['id'], line['fc'])
        db.session.add(fc)
        db.session.commit()

    for line in result:
        cap_pool = CapPool(line['id_cap_pool'], line['cap_pool_name'])
        db.session.add(cap_pool)
        db.session.commit()

    for line in result:
        cap_horaire = CapHoraire(line['id_cap_horaire'], line['cap_value'], line['cap_timestamp'], line['user_id'])
        db.session.add(cap_horaire)
        db.session.commit()
    for line in result:
        group = CapHoraire(line['id_group'], line['group_name'], line['group_type'])
        db.session.add(group)
        db.session.commit()




#@app.route('/FlightCompany', methods=['GET'])
#def get_flightCompany():
    #return Vol.query.filter_by(fc).distinct()

@app.route('/flights', methods=['GET'])
def flights():
    data = {'flights':[{'time':'5:30', 'flightNumber':'AC130', 'destination':'YPO'},
    {'time':'6:30', 'flightNumber':'AB230', 'destination':'GHR'},
    {'time':'6:40', 'flightNumber':'AS550', 'destination':'DSW'},
    {'time':'6:55', 'flightNumber':'AG840', 'destination':'HGR'},
    {'time':'7:10', 'flightNumber':'AW430', 'destination':'NBV'}]}

    return jsonify(data)

def get_user():
    if 'Api_Access_Token' not in request.headers or 'Api_Username' not in request.headers:
        return return_error()
    else:
        token = request.headers['Api_Access_Token']
        username = request.headers['Api_Username']
        return username
    return None

@app.route('/assign', methods=['GET', 'POST'])
def assign():
    user = get_user()
    if request.method == 'GET':
        data = {'flightCount':0}
        data1 = {'flightCount':3}
        data2 = {'flightCount':1}
        if user=="1":
            data = data1
        elif user=="2":
            data=data2
        return jsonify(data)
    elif request.method == 'POST':
        print('POST')
        for key in request.args:
            print(key)
        acceptedFlights = request.form['values']
        print(acceptedFlights)
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
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        print('Username or Password is invalid')
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    return jsonify({'token': '123','username': registered_user.username})

def return_error():
    return jsonify({'error': 'you do not have access'})



@app.route("/userLogged")
def userLogged(user=None):
    return user.username

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return ""

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8932)
