#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from collections import defaultdict
from flask import Flask, request, render_template, make_response
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

        style = get_style()
        result = generate_result(form, style)
        return render_template('index.html', request=request.form, result=result.decode('utf-8'))
    except:
        return traceback.format_exc()

@app.route('/style/', methods=['GET', 'POST'])
def style_template():
    try:
        style = get_style()
        resp = make_response(render_template('style.html', style=style.unicode_dict()))
        resp.set_cookie('h1_template', style.h1_template)
        resp.set_cookie('h2_template', style.h2_template)
        resp.set_cookie('footer', style.footer)
        return resp
    except:
        return traceback.format_exc()

def get_style():
    style = Style()
    style.h1_template = update_from_cookie_and_post(style.h1_template, 'h1_template')
    style.h2_template = update_from_cookie_and_post(style.h2_template, 'h2_template')
    style.footer      = update_from_cookie_and_post(style.footer, 'footer')
    return style

def update_from_cookie_and_post(var, key):
    if request.cookies.get(key):
        var = request.cookies.get(key).encode('utf-8')
    if request.form.get(key):
        var = request.form.get(key).encode('utf-8')
    return var

