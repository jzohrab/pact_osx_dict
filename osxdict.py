import sys
import os
import re
import unicodedata

sys.path.append(os.path.join(os.path.dirname(__file__), "vendor"))
from macdict import lookup_word

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def lookup(word):
    w = remove_accents(word).decode("utf-8")
    print(f'looking up: {w}')
    definition = lookup_word(w)
    if definition:
        definition = re.sub(r'\.\s+', '.\n', definition)
    return definition

if __name__ == '__main__':
    word = sys.argv[1]
    d = lookup(word)
    print('---')
    print(d)
