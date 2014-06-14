#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implement the style function."""

class Style:
    """Implement the template style.
    Users can design their own style with some strings to be replaced."""

    DEFAULT_STR = '標題'
    DEFAULT_H1 = '【*[1;33m標題*[m】\n'.format(DEFAULT_STR)
    DEFAULT_H2 = '*[1;36m◎{0}*[m\n'.format(DEFAULT_STR)
    DEFAULT_FOOTER = '''
*[m
  *[47m                *[46m                                                  *[m
  *[30;47m  【鄉民日報】  *[1;37;46m   做個活活潑潑的好鄉民，當個堂堂正正的台灣人。   *[m
  *[47m                *[46m                                                  *[m
*[m





鍵在手，跟我走~滅壟斷，奪主流!


                          鍵在手，跟我走~滅壟斷，奪主流!


                                              鍵在手，跟我走~滅壟斷，奪主流

                                                            http://ppt.cc/e9Bg

'''

    def __init__(self, h1=DEFAULT_H1, h2=DEFAULT_H2, footer=DEFAULT_FOOTER):
        self.h1_template = h1
        self.h2_template = h2
        self.footer = footer

    def h1(self, s):
        return self.render(self.h1_template, s.strip())

    def h2(self, s):
        return self.render(self.h2_template, s.strip())

    def render(self, template, in_string):
        """Generator a converting function."""
        return template.replace(self.DEFAULT_STR, in_string)

    def unicode_dict(self):
        """Convert the template string to unicode."""
        return {
            'h1_template' : self.h1_template.decode('utf-8'),
            'h2_template' : self.h2_template.decode('utf-8'),
            'footer'      : self.footer.decode('utf-8'),
        }


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
*[m
*[0;1;30m  ██￣╲ ￣██￣ ￣██￣   ██￣╲          ￣￣ ██*[m
*[0;1;30m  ██  ▕   ██     ██     ██  ▕ ╱￣█◣ ██ ██ ▏  ██*[m
*[0;1m  ██ˍ╱   ██     ██     ██  ▕ ╱￣██ ██ ██ ▏  ██*[m
*[0;1m  ██       ██     ██     ██ˍ╱ ╲ˍ██ ██ ██ ╲ˍ██ #{2}*[m
                                                           *[0;1m╲ˍ█◤           *[0m　*[m
  *[m{0}ψ{1}*[m
*[m
  *[41m                                                                *[m
'''.format(date, author, number)
    ret += '  *[1;41m  ◆ {0}*[m\n'.format(fill_string(headlines[0], COUNT))
    ret += '''  *[41m                                                                *[m
  *[0;31m┌───────────────────────────────┐*[m
  *[0;31m│                                                              │*[m
'''
    for line in headlines[1:]:
        ret += '  *[0;31m│ *[0m{0} *[0;31m │*[m\n'.format(fill_string(line, COUNT))
    ret += '''  *[0;31m│                                                              │*[m
  *[0;31m└───────────────────────────────┘*[m

'''
    return ret

