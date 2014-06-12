#!/usr/bin/env python
# -*- coding: utf-8 -*-

ESC = '\025' # ctrl-U
"""黑紅綠黃藍紫靛白"""
BLACK  = 0
RED    = 1
GREEN  = 2
YELLOW = 3
BLUE   = 4
PURPLE = 5
INDIGO = 6
WHITE  = 7

def colorCode(front=WHITE, back=BLACK, highlight=False):
    front_code = front + 30
    back_code = back + 40
    highlight_code = 1 if highlight else 0
    return '{0}[{1};{2};{3}m'.format(ESC, highlight_code, front_code, back_code)

