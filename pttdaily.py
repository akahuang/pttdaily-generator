#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert the markdown to ptt-style output."""
import style

def generate_result(form):
    """Convert the request to the PTT-style result."""
    author = form['author']
    date = form['date']
    number = form['number']
    headline = form['headline']
    content = form['content']

    ret = ''
    ret += style.header(author, number, date, headline)
    for line in content.split('\n'):
        if line[:2] == '##':
            line = style.h2(line[2:])
        elif line[:1] == '#':
            line = style.h1(line[1:])
        ret += line
    ret += style.footer()

    return ret


