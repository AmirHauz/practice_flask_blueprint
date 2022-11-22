from flask import Blueprint, render_template

cats = Blueprint('/cats', __name__,url_prefix='/cats')

@cats.route('')
@cats.route('/')
def cats1():
    return render_template("cats.html")

@cats.route('/sale4')
def sale_4():
    return render_template("sale4.html")

@cats.route('/sale5')
def sale_5():
    return render_template("sale5.html")

@cats.route('/sale6')
def sale_6():
    return render_template("sale6.html")