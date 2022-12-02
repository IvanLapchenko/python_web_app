from app import app
from flask import render_template



@app.route("/index")
@app.route("/static/index.html")
@app.route("/")
def index():
    user = {"username": "Nik", "age": "40"}
    posts = [
        {
            "author": {"username": "Sarah", "age": "20"},
            "body": "I like Avengers"
        },
        {
            "author": {"username": "Lora", "age": "30"},
            "body": "I like Batman"
        },
        {
            "author": {"username": "John", "age": "25"},
            "body": "I like both"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)







# @app.route("/static/first.html")
# def func():
#     return render_template("first.html")
#
#
# @app.route("/static/second.html")
# def func1():
#     return render_template("second.html")
#
# @app.route("/name")
# @app.route("/contacts")
# def contacts():
#     return "This is contacts page"
#
#
# @app.route("/yellow")
# @app.route("/blue")
# def contacts1():
#     return "This yellow and blue page"
#
#
# @app.route("/services")
# def services():
#     return "This is services page"
#
#
# @app.route("/services/<first>/<second>")
# def detailed_services(first, second):
#     summ = str(int(first) + int(second))
#     return summ