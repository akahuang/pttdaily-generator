#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implement the style function."""

from time import strftime
from ansi import ESC

def h1(string):
    string = string.strip()
    return '{0}[46m  {0}[47m {0}[30m{1}  {0}[m\n'.format(ESC, string)

def h2(string):
    string = string.strip()
    return '{0}[1;36m◎{1}{0}[m\n'.format(ESC, string)

def fill_string(string, length):
    """Fill space until the length.
    Ex: fill_string('abc', 5)  => 'abc  '
        fill_string('你好', 5) => '你好 ' 
        fill_string('啦啦啦超過啦', 4) => Exception XDD
    """
    current_length = len(string.decode('utf-8').encode('big5'))
    return string + ' ' * (length - current_length)

def header(author, number, date):
    """ptt daily首頁."""
    ret = '''
{0}[m
{0}[0;1;30m  ██￣╲ ￣██￣ ￣██￣   ██￣╲          ￣￣ ██{0}[m
{0}[0;1;30m  ██  ▕   ██     ██     ██  ▕ ╱￣█◣ ██ ██ ▏  ██{0}[m
{0}[0;1m  ██ˍ╱   ██     ██     ██  ▕ ╱￣██ ██ ██ ▏  ██{0}[m
  {0}[0;1m██       ██     ██     ██ˍ╱ ╲ˍ██ ██ ██ ╲ˍ██ #{3}{0}[m
                                                           {0}[0;1m╲ˍ█◤           {0}[0m　{0}[m
  {1}ψ{2}{0}[m
{0}[m
   {0}[41m                                                                {0}[m
   {0}[1;41m  ◆立法院臨時會，倒數四天！                                    {0}[m
   {0}[41m                                                                {0}[m
  {0}[0;31m┌───────────────────────────────┐{0}[m
  {0}[0;31m│                                                              │{0}[m
  {0}[0;31m│ {0}[0;1;31m立院臨時會 馬下令：過服貿、擋投票年齡下修 {0}[0m
  {0}[0;31m│                                                              │{0}[m
  {0}[0;31m│ {0}[0;1;31m臨時會前 民進黨擴大會議凝聚共識 {0}[0mhttp://ppt.cc/-idZ
  {0}[0;31m│                                                              │{0}[m
  {0}[0;31m│ {0}[0m閉門會議將針對：考、監兩院人事同意權                         {0}[m
  {0}[0;31m│ {0}[0m兩岸協議監督條例，及兩岸服務貿易協議等4大議題交換意見，      {0}[m
  {0}[0;31m│ {0}[0m凝聚黨內共識，並討論相關議事攻防。                           {0}[m
  {0}[0;31m│                                                              │{0}[m
  {0}[0;31m└───────────────────────────────┘{0}[m

'''.format(ESC, date, author, number)
    return ret

def footer():
    """Ptt Daily 頁尾"""
    ret = '''
{0}[m
  {0}[47m                {0}[46m                                                  {0}[m
  {0}[30;47m  【鄉民日報】  {0}[1;37;46m   做個活活潑潑的好鄉民，當個堂堂正正的台灣人。   {0}[m
  {0}[47m                {0}[46m                                                  {0}[m
{0}[m
'''.format(ESC)
    return ret
