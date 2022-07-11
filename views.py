from flask import Flask, Blueprint, render_template, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template ("index.html")