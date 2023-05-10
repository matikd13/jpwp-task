import requests
from flask import Flask, Response

app = Flask(__name__)


@app.route('/', methods=['GET'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    resp = requests.get(f'https://agh.edu.pl/{path}')
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
    return response
