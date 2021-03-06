#!/usr/local/pythonenv/pylukinlib/bin/python
"""
Demonstrating the login blueprint using flask-login.

"""

__author__ = "daniel.lindh@renter.se"
__copyright__ = "Copyright 2015, Renter AB"

from flask import Flask, url_for
from flask.ext.login import login_required

from pylukinlib.flask.blueprint import login


app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,

    # Generate a new secret key every time the wsgi are restarted. This
    # will invalidate all sessions between restarts.
    SECRET_KEY='\xe8.\xcf_\xef\n\nQ1\xe8\xca\xcd\xef\x12\x9e\xa2\xd96_\xdeM"\x97\xde'
))

login.init_app(app, "index", {"user": "password"})
app.register_blueprint(login.login_pages)


@app.route('/')
@login_required
def index():
    return 'Hello World! <a href="%s">logout</a>' % url_for('login_pages.logout')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
