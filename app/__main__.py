from flask import Flask
from flask import render_template
from flask import request
from controllers \
    import \
        (IndexController,
        SentimentController,
        EntityController,
        AnalyzeController,
        SendController)

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    c = IndexController()
    responses = c.index()
    return render_template('hello.html', responses=responses)

@app.route('/sentiment', methods = ['GET'])
def sentiment():
    s = SentimentController()
    responses = s.index()
    return render_template('sentiment.html', responses=responses)

@app.route('/analyze', methods = ['GET','POST'])
def analyze():
    s = AnalyzeController()
    entities, types, sentiments = s.index()
    return render_template('analyze.html', responses=sentiments, entities=entities, types=types, method=request.method)

@app.route('/sending', methods = ['GET','POST'])
def sending():
    s = SendController()
    s.index()
    return render_template('sending.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
