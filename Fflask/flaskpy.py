from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/article123/<any(str(1),str(2)):id>/<age>')
# @app.route('/article123/<uuid:id>/<age>')
def article1(id, age):
    print(type(id))
    return '%s article detail' % id

# 反向解析
@app.route('/')
def index():
    print(url_for("article1", id=1, age=18000))
    return redirect(url_for("article1", id=str(1), age=180001))


if __name__ == '__main__':
    app.run(port=1234, debug=True)
