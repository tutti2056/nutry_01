from flask import render_template
from testapp import app

@app.route("/")
def index():
    my_dict = {
        'insert_something1': '1週間の摂取栄養量を計算します。',
        'insert_something2': '1週間の摂取栄養量を計算します。02',
        'test_titles': ['title1', 'title2', 'title3']
    }
    return render_template('testapp/index.html', my_dict=my_dict)

@app.route("/test")
def test01():
    return render_template('testapp/index2.html')
