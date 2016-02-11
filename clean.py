import re
import os


def remove_pagenos():
    os.chdir('cases/')
    list_dir = os.listdir('.')

    for filename in list_dir:
        f = open(filename, 'r')
        temp = f.read()
        f.close()

        g = re.findall(r'\n+.+?Page.+?\n', temp)
        for elem in g:
            temp.replace(elem, " ")
        w = open(filename + 'clean', 'w')
        w.write(temp)
        w.close()

if __name__ == '__main__':
    remove_pagenos()
