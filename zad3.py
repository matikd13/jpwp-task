import requests
from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/', methods=['GET'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    domena = request.headers['Host'].split(":")[0]

    cel = ""

    if domena == "localhost":
        cel = "https://jakubowskii.pl"
    elif domena == "127.0.0.1":
        cel = "https://agh.edu.pl"
    else:
        return Response("404 Nie ma takiej strony", 404)

    resp = requests.get(f'{cel}/{path}')
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
    return response
