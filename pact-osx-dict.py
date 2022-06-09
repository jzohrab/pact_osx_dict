import sys
import os
import re

sys.path.append(os.path.abspath(sys.path[0]) + '/vendor')
from macdict import lookup_word


def lookup(word):
    definition = lookup_word(word)
    if definition:
        definition = re.sub(r'\.\s+', '.\n\n', definition)
    return definition


if __name__ == '__main__':
    word = sys.argv[1]
    d = lookup(word)
    print('---')
    print(d)
