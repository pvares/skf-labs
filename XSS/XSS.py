import os
import hmac
import hashlib
import base64

from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

def gen_flag():
    secret = os.environ["secret_key"]
    hm = hmac.new(secret.encode('utf8'), b"xss", "sha256")
    return hm.hexdigest()

@app.route("/home", methods=['POST'])
def home():
    xss = request.form['string']
    # SENG-1712
    if app.jinja_env.from_string("{{xss|e}}").render(xss=xss) != app.jinja_env.from_string("{% autoescape false %}{{xss}}{% endautoescape %}").render(xss=xss):
        flag = gen_flag()
    else:
        flag = ""

    return render_template("index.html",xss=xss, flag=flag)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
