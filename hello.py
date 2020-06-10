import datetime
from flask import Flask, render_template, request, session, redirect
from flask_session import Session

app = Flask(__name__)

app.config["SESSION PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    headline = "Hello!"
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    
    return render_template("index.html", headline=headline, notes=notes)


@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"

@app.route("/time")
def time():
    now = datetime.datetime.now()
    time = now.month == 5 and now.day == 18
    return render_template("time.html", time=time, now=now)

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("test.html", name=name)

@app.route('/foo')
def foo():
    return session.sid


@app.route('/bar')
def bar():
    return session.sid
