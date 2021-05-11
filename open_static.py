#!/usr/bin/env python

import flask
import random
import pathlib

root = str(pathlib.Path(__file__).parent.resolve())
stem = pathlib.Path(__file__).parent.stem

app = flask.Flask(__name__, static_folder=root, static_url_path=f'/{stem}', template_folder=root)


@app.route('/')
def index():
    return flask.render_template('index.html')


port = int(5000 + 5000*random.random())
app.run(debug=True, port=port)
