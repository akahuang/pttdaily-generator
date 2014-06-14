#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implement the style function."""

class Style:
    """Implement the template style.
    Users can design their own style with some strings to be replaced."""

    DEFAULT_STR = '標題'
    DEFAULT_H1 = '\025[46m  \025[47m \025[30m{0}  \025[m\n'.format(DEFAULT_STR)
    DEFAULT_H2 = '\025[1;36m◎{0}\025[m\n'.format(DEFAULT_STR)
    DEFAULT_FOOTER = '''\025[m
  \025[47m                \025[46m                                                  \025[m
  \025[30;47m  【鄉民日報】  \025[1;37;46m   做個活活潑潑的好鄉民，當個堂堂正正的台灣人。   \025[m
  \025[47m                \025[46m                                                  \025[m
\025[m
'''

    def __init__(self, h1=DEFAULT_H1, h2=DEFAULT_H2, footer=DEFAULT_FOOTER):
        self.h1 = self.generate_converter(h1)
        self.h2 = self.generate_converter(h2)
        self.footer = footer

    def generate_converter(self, string):
        """Generator a converting function."""
        return lambda s: string.replace(self.DEFAULT_STR, s)


def h1(string):
    string = string.strip()
    return '\025[46m  \025[47m \025[30m{0}  \025[m\n'.format(string)

def h2(string):
    string = string.strip()
    return '\025[1;36m◎{0}\025[m\n'.format(string)

def fill_string(string, length):
    """Fill space until the length.
    Ex: fill_string('abc', 5)  => 'abc  '
        fill_string('你好', 5) => '你好 '
        fill_string('啦啦啦超過啦', 4) => '啦啦'
        fill_string('啦啦啦不用補空白', -1) => '啦啦啦不用補空白'
    """
    string = string.strip()
    current_length = len(string.decode('utf-8').encode('big5'))
    if length > current_length:
        return string + ' ' * (length - current_length)
    else:
        return string

def header(author, number, date, headline):
    """ptt daily首頁."""
    COUNT = 59
    headlines = headline.split('\n')

    ret = '''
\025[m
\025[0;1;30m  ██￣╲ ￣██￣ ￣██￣   ██￣╲          ￣￣ ██\025[m
\025[0;1;30m  ██  ▕   ██     ██     ██  ▕ ╱￣█◣ ██ ██ ▏  ██\025[m
\025[0;1m  ██ˍ╱   ██     ██     ██  ▕ ╱￣██ ██ ██ ▏  ██\025[m
\025[0;1m  ██       ██     ██     ██ˍ╱ ╲ˍ██ ██ ██ ╲ˍ██ #{2}\025[m
                                                           \025[0;1m╲ˍ█◤           \025[0m　\025[m
  \025[m{0}ψ{1}\025[m
\025[m
  \025[41m                                                                \025[m
'''.format(date, author, number)
    ret += '  \025[1;41m  ◆ {0}\025[m\n'.format(fill_string(headlines[0], COUNT))
    ret += '''  \025[41m                                                                \025[m
  \025[0;31m┌───────────────────────────────┐\025[m
  \025[0;31m│                                                              │\025[m
'''
    for line in headlines[1:]:
        ret += '  \025[0;31m│ \025[0m{0} \025[0;31m │\025[m\n'.format(fill_string(line, COUNT))
    ret += '''  \025[0;31m│                                                              │\025[m
  \025[0;31m└───────────────────────────────┘\025[m

'''
    return ret

def footer():
    """Ptt Daily 頁尾"""
    ret = '''
\025[m
  \025[47m                \025[46m                                                  \025[m
  \025[30;47m  【鄉民日報】  \025[1;37;46m   做個活活潑潑的好鄉民，當個堂堂正正的台灣人。   \025[m
  \025[47m                \025[46m                                                  \025[m
\025[m
'''
    return ret
