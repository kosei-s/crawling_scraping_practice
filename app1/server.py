from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list', methods=['POST'])
def list():
    url = request.form['URL']
    res = requests.get(url)

    try:
        res.raise_for_status()
    except Exception as exc:
        render_template('index.html')
    
    return render_template('list.html', url=url)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)