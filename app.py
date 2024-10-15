# app.py
from flask import Flask, render_template, make_response, abort
from werkzeug.wrappers import Request, Response


class redir_middleware():
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        if req.host == "hello-flask-roadmr":
            res = Response("", status=301, location="https://yahoo.com")
            return res(environ, start_response)
        return app(self.app, start_response)


app = Flask(__name__)

#app.wsgi_app = redir_middleware(app.wsgi_app)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
#    abort(503)
#    time.sleep(130)
    with open("./foo.bar", "wb") as baz:
        baz.write(b"yeye")
    with open("./templates/foo.bar", "wb") as baz:
        baz.write(b"meye")
    return make_response(render_template('hello.html', name=name))

@app.route('/redirect/')
def redir(name=None):
    return make_response("hi there")
