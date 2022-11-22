from flask import Blueprint, render_template

dogs = Blueprint('/dogs', __name__,url_prefix='/dogs')

@dogs.route('')
@dogs.route('/')
def dogs1():
    return render_template("dogs.html")

@dogs.route('/sale1')
def sale_1():
    return render_template("sale1.html")

@dogs.route('/sale2')
def sale_2():
    return render_template("sale2.html")

@dogs.route('/sale3')
def sale_3():
    return render_template("sale3.html")