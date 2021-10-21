from flask import Flask,render_template
from BP.main import main
app = Flask(__name__)


app = Flask(__name__)
app.register_blueprint(main, url_prefix="/requests")


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/exit')
def goodbye():
    return render_template('exit_page.html')


if __name__ == '__main__':
    app.run()
