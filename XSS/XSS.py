from flask import Flask, request, url_for, render_template, redirect
import bleach

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

def gen_flag():
    #idk
    print("flag!!!")

@app.route("/home", methods=['POST'])
def home():
    xss = request.form['string']
    if bleach.clean(xss) != xss:
        gen_flag()
    return render_template("index.html",xss = xss)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
