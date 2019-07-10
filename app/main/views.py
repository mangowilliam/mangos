from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/js')
def js():
    return render_template("js.html")
