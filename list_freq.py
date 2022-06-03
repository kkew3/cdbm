import sys
import json


filename = sys.argv[1]
with open(filename, encoding='utf-8') as infile:
    freq = list(json.load(infile).items())
if freq:
    freq.sort(key=lambda x: x[1], reverse=True)
    freq = [(key, str(count)) for key, count in freq]
    max_width_count = max([len(x[1]) for x in freq])
    for key, count in freq:
        print('{} {}'.format(count.rjust(max_width_count), key))
