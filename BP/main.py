from flask import Blueprint, render_template, request

from UserDatabase import work_with_db

main = Blueprint('main', __name__, template_folder='./templates', static_folder='./static')
dbconfig = {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': "password", 'db': 'new_schema'}


@main.route('/')
def request_choice():
    return render_template('request_choice.html')


@main.route('/request1', methods=('GET', 'POST'))
def request1():
    if request.method == 'POST':
        text1 = request.form.get('request1_text')
        text2 = request.form.get('request2_text')
        _SQL_ = "select * from new_schema.order where date between '%s' and '%s'"
        result = work_with_db(dbconfig, _SQL_, (text1, text2))
        return render_template('request_result.html', result=result)

    return render_template('request1.html')


@main.route('/request2', methods=('GET', 'POST'))
def request2():
    if request.method == 'POST':
        text = request.form.get('request2_text')
        _SQL_ = "select * from new_schema.room_cleaning where service_id ='%s'"
        result = work_with_db(dbconfig, _SQL_, text)
        return render_template('request_result.html',result=result)

    return render_template('request2.html')
