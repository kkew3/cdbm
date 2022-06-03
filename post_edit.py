import sys
import json


cdbm_file = sys.argv[1]
freq_file = sys.argv[2]
present_keys = set()
with open(cdbm_file, encoding='utf-8') as infile:
    for line in infile:
        if line.startswith('#'):
            line = line[1:]
        present_keys.add(line.split(maxsplit=1)[0])
with open(freq_file, encoding='utf-8') as infile:
    freq = json.load(infile)
visited_keys = set(freq)
visited_keys -= present_keys  # now visited_keys are keys not present any more
for key in visited_keys:
    del freq[key]
with open(freq_file, 'w', encoding='utf-8') as outfile:
    json.dump(freq, outfile)
