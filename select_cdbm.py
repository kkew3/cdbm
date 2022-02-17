import sys


cdbm_file = sys.argv[1]
selected_key = sys.argv[2]
with open(cdbm_file) as infile:
    for line in infile:
        if not line.startswith('#'):
            tokens = line.split(maxsplit=1)
            if tokens[0] == selected_key:
                if len(tokens) > 1:
                    sys.stdout.write(tokens[1])
                break
