import sys
import json


cdbm_file = sys.argv[1]
selected_key = sys.argv[2]
freq_file = sys.argv[3] if len(sys.argv) >= 4 else None
found = False
with open(cdbm_file) as infile:
    for line in infile:
        if not line.startswith('#'):
            tokens = line.split(maxsplit=1)
            if tokens[0] == selected_key:
                if len(tokens) > 1:
                    sys.stdout.write(tokens[1])
                found = True
                break
if freq_file and found:
    try:
        with open(freq_file, encoding='utf-8') as infile:
            freq = json.load(infile)
    except FileNotFoundError:
        freq = {}
    freq[selected_key] = freq.get(selected_key, 0) + 1
    with open(freq_file, 'w', encoding='utf-8') as outfile:
        json.dump(freq, outfile, indent=2)
