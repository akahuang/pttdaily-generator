#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from collections import defaultdict
from flask import Flask, request, render_template
from pttdaily import generate_result
from style import Style

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.form.get('action') is None:
        return render_template('index.html', request=defaultdict(str), result='')
    try:
        form = {
            'author'   : request.form.get('author', '').encode('utf-8'),
            'date'     : request.form.get('date', '').encode('utf-8'),
            'number'   : request.form.get('number', '').encode('utf-8'),
            'headline' : request.form.get('headline', '').encode('utf-8'),
            'content'  : request.form.get('content', '').encode('utf-8'),
        }

        result = generate_result(form)
        return render_template('index.html', request=request.form, result=result.decode('utf-8'))
    except:
        return traceback.format_exc()

@app.route('/style/', methods=['GET', 'POST'])
def style_template():
    style = Style()
    style.toUnicode()
    try:
        return render_template('style.html', style=style)
    except:
        return traceback.format_exc()
