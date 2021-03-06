from flask import Flask, render_template, request
import requests, bs4

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list', methods=['POST'])
def list():
    url = request.form['URL']

    try:
        res = requests.get(url)
    except Exception as exc:
        return '正しいURLを入力してください'

    try:
        res.raise_for_status()
    except Exception as exc:
        return '正しいURLを入力してください'
    
    soup = bs4.BeautifulSoup(res.text)
    link_elems = soup.select('a')
    link_urls = []
    for i in range(len(link_elems)):
        link_urls.append(link_elems[i].get('href'))
    
    return render_template('list.html', url=url, link_urls=link_urls)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)