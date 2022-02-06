import sys


cdbm_file = sys.argv[1]
with open(cdbm_file) as infile:
    key_width = 0
    for line in infile:
        key_width = max(key_width, len(line.split(maxsplit=1)[0]))
    infile.seek(0)
    for line in infile:
        tokens = line.split(maxsplit=1)
        sys.stdout.write('\033[1;31m{}\033[0m {}'.format(
            tokens[0].ljust(key_width), ''.join(tokens[1:]) or '\n'))
