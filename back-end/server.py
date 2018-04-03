#!flask/bin/python
import flask
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'super secret key'
login_manager = LoginManager()
login_manager.init_app(app)
CORS(app)
programming = Programming()

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
        if (programming.logIn(request.form["username"], request.form["hashedPassword"])) != None:
            u = User(programming.logIn(request.form["username"], request.form["hashedPassword"])["id"])
            login_user(u)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        #if not is_safe_url(next):
        #    return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return ""

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8932)
