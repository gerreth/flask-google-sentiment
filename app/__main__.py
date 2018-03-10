from flask import Flask
from flask import render_template
from flask import request
from controllers \
    import \
        (IndexController)

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    c = IndexController()
    responses = c.index()
    return render_template('hello.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
