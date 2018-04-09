#!flask/bin/python
import flask
from flask import Flask, jsonify, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required, login_user, logout_user, current_user


from hashlib import md5
from datetime import datetime
from functools import wraps
from db import db
from vol import Vol
from airport import Airport

app = Flask(__name__)
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postTrans@localhost:5432/postgres'
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

CORS(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)

    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
        self.access_token = "123"

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return chr(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

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
    db.create_all()
    return "Hello, World!"

@app.route('/assets', methods=['GET'])
def get_assets():
    return "no assets"

@app.route('/FlightCompany', methods=['GET'])
def get_assets():
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

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """Check if api_access_token and api_username
           headers are setted and check credentials
        """
        if 'api_access_token' not in request.headers or 'api_username' not in request.headers:
            return return_error()
        else:
            token = request.headers['api_access_token']
            username = request.headers['api_username']
            try:
                user = User.query.filter_by(username=username).first()
                kwargs['user'] = user
                return f(*args, **kwargs)
            except Exception as error:
                #import ipdb; ipdb.set_trace()
                return return_error()
    return decorated_function

@app.route("/userLogged")
@auth_required
def userLogged(user=None):
    return user.username

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return ""

from admin_constante_hyst   import AdminCsteHyst

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8932)
