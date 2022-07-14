from flask import Flask, Blueprint, render_template, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template ("index.html")

@my_view.route('/home')
@my_view.route('/hoe')
@my_view.route('/hme')
@my_view.route('/ome')
def index_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route('/legends')
def legends():
    return render_template ("legends.html")

@my_view.route('/legend')
@my_view.route('/legens')
@my_view.route('/legeds')
@my_view.route('/legnds')
@my_view.route('/leends')
@my_view.route('/lgends')
@my_view.route('/egends')
@my_view.route('/')
def page1_redirect():
    return redirect(url_for("my_view.legends"))

@my_view.route('/maps')
def maps():
    return render_template("maps.html")

@my_view.route('/map')
@my_view.route('/mas')
@my_view.route('/mps')
@my_view.route('/aps')
def maps_redirect():
    return redirect(url_for("my_view.maps"))

@my_view.route('/weopons')
def weopons():
    return render_template("weopons.html")

@my_view.route('/weopon')
@my_view.route('/weopos')
@my_view.route('/weopns')
@my_view.route('/weoons')
@my_view.route('/wepons')
@my_view.route('/wopons')
@my_view.route('/eopons')
def weopons_redirect():
    return redirect(url_for("my_view.weopons"))

@my_view.route('/about')
def about():
    return render_template("about.html")

@my_view.route('/abou')
@my_view.route('/abot')
@my_view.route('/abut')
@my_view.route('/aout')
@my_view.route('/bout')
def about_redirect():
    return redirect(url_for("my_view.about"))