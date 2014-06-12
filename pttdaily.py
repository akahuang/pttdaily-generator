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
    ret += style.header(author, number, date)
    for line in content.split('\n'):
        if line[:2] == '##':
            line = style.h2(line[2:])
        elif line[:1] == '#':
            line = style.h1(line[1:])
        ret += line
    ret += style.footer()

    print 'type(ret):', type(ret)
    return ret



#def main(argv=sys.argv[:]):
#    if len(argv) <= 2:
#        return 'Usage: {0} <input> <output>'.format(argv[0])
#    infile, outfile = argv[1:]
#
#    author = 'TestAuthor' 
#    number = 14
#    with open(infile, 'r') as fin:
#        fout = open(outfile, 'w')
#        fout.write(style.header(author, number))
#        for line in fin:
#            if line[:2] == '##':
#                line = style.h2(line[2:])
#            elif line[:1] == '#':
#                line = style.h1(line[1:])
#            fout.write(line)
#
#        fout.write(style.footer())
#
#    return 0
#
#if __name__ == '__main__':
#    sys.exit(main())
#
