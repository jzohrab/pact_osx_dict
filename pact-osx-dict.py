import sys
import os

sys.path.append(os.path.abspath(sys.path[0]) + '/vendor')
from macdict import lookup_word

word = sys.argv[1]
definition = lookup_word(word)
if definition:
    definition = definition.replace('.', '.\n\n')
print(definition)
