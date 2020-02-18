from flask import Flask, request, url_for, render_template, redirect
from subprocess import call
import os
import hmac

def gen_flag():
    secret = os.environ["secret_key"]
    hm = hmac.new(secret.encode('utf8'), b"auth-missing", "sha256")
    return hm.hexdigest()

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():

    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    url = request.form['pois_url']
    return render_template("index.html", url=url)


@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    return render_template("user_created_right.html", username=username)


@app.route("/users/<user_id>", methods=['GET'])
def load_account(user_id):

    if user_id == "user01":
        username = "bob"
        password = "abcd1234"
        data = "Your secret message: [STILL NOT SET]"
        return render_template("useraccount.html", username=username, password=password, data=data, flag=gen_flag())

    elif user_id == "user02":
        username = "admin"
        password = "rootadmin"
        data = "I am the admin of this website."
        return render_template("useraccount.html", username=username, password=password, data=data, flag=gen_flag())
    else:
        username = "You need to set your usser account"
        password = "You need to set your password"
        data = "You need to set your data"
        return render_template("useraccount_empty.html", username=username, password=password, data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
