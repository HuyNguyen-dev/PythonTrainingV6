from app import app
from flask import render_template


def home():
    return render_template("index.html")


def about():
    return "About page"

def login():
    return render_template('login.html')
