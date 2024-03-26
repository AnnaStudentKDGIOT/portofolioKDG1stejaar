import flask

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    html = "<html><body><h1>"
    html = (html + '<h1>Hallo dit is de pagina van Anna Johnson</h1>' +
            '<img src="/static/images/bears-1708944798533-9198.jpg" alt="bear" '
            'height="460" width="500">'
            + '<br>'+ '<br>'+'<a href="https://www.google.com/search?q=Anna+Ella+Johnson&oq=Anna+Ella+Johnson&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIKCAMQABiABBiiBDIKCAQQABiABBiiBDIGCAUQRRg9MgYIBhBFGD0yBggHEEUYPTIGCAgQRRhA0gEINzkyMWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8" target="_blank">Anna johnson</a>')
    html = html + '</body></html>'
    return html
