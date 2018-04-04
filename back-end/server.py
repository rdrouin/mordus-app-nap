#!flask/bin/python
import flask
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from user import User
from hashlib import md5

app = Flask(__name__)
app.secret_key = 'super secret key'
login_manager = LoginManager()
login_manager.init_app(app)
CORS(app)

# TODO with postgresql
h = md5()
h.update(b'user')
h.hexdigest()
userlist = [User("user", h.hexdigest())]
print(User("user", h.hexdigest()) in userlist)
print(User("user", 'ee11cbb19052e40b07aac0ca060c23ee' ) in userlist)
print(h.hexdigest())

@login_manager.user_loader
def load_user(user_id):
    if user_id in userlist:
        return next(x for x in userlist if x == user_id)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/assets', methods=['GET'])
def get_assets():
    return "no assets"

@app.route('/search/<searchText>', methods=['GET'])
def get_searchTitles(searchText):
    return "assets serach :" + str(searchText)

@app.route('/login', methods=['POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    if True:
        # Login and validate the user.
        # user should be an instance of your `User` class
        # validate data
        if "username" in request.form and "hashedPassword" in request.form:
            if User(request.form["username"], request.form["hashedPassword"]) in userlist:
                u = User(request.form["username"], request.form["hashedPassword"])
                u.is_active = True
                login_user(u)
                print('Logged in successfully.')
                flask.flash('Logged in successfully.')
            else:
                print('Username not found')
                flask.flash('Username not found')
        else:
            flask.flash('format invalid')
            print('format invalid')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        #if not is_safe_url(next):
        #    return flask.abort(400)

        return flask.redirect(next or flask.url_for('userLogged'))
    return flask.render_template('login.html', form=form)

@app.route("/userLogged")
def userLogged():
    if current_user.get_id() == None:
        return "The user logged is anonymous "
    else:
        return "The user logged is " + current_user.get_id()

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return ""

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8932)
