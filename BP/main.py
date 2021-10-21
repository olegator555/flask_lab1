from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='./templates', static_folder='./static')


@main.route('/')
def request_choice():
    return render_template('request_choice.html')


@main.route('/request1')
def request1():
    return render_template('request1.html')


@main.route('/request2')
def request2():
    return render_template('request2.html')
