#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import traceback
from collections import defaultdict
from flask import Flask, request, render_template, make_response
from pttdaily import generate_result
from style import Style

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    try:
        if request.form.get('action') is None:
            default_value = defaultdict(str)
            default_value['author'] = 'meowmeowgo'
            default_value['date'] = datetime.today().strftime('%Y.%m.%d')
            default_value['number'] = default_number(datetime.today())
            default_value['content'] = default_title(['活動', '社會', '政治', '公民', '國際', '溫馨', '娛樂', '八卦'])
            return render_template('index.html', request=default_value, result='')

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

@app.route('/help/', methods=['GET'])
def help_page():
    return render_template('help.html')

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


def default_title(title_list):
    return ''.join(map(lambda s: '# ' + s + '版\n\n\n', title_list)).decode('utf-8')

def default_number(current_date):
    """The first date is 2014.05.30."""
    ZERO_DATE = datetime.strptime('2014.05.29', '%Y.%m.%d')
    return (current_date - ZERO_DATE).days
