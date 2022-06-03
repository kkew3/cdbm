import sys
import shutil

if sys.platform == 'win32':
    import colorama
    colorama.init()
else:
    try:
        import colorama
    except ImportError:
        pass
    else:
        colorama.init()

cdbm_file = sys.argv[1]

if sys.stdout.isatty():
    with open(cdbm_file, encoding='utf-8') as infile:
        key_width = 0
        for line in infile:
            if not line.startswith('#'):
                key_width = max(key_width, len(line.split(maxsplit=1)[0]))
        infile.seek(0)
        for line in infile:
            if line.startswith('#'):
                sys.stdout.write('\033[90m{}\033[0m'.format(line))
            else:
                tokens = line.split(maxsplit=1)
                sys.stdout.write('\033[1;31m{}\033[0m {}'.format(
                    tokens[0].ljust(key_width), ''.join(tokens[1:]) or '\n'))
else:
    with open(cdbm_file, encoding='utf-8') as infile:
        shutil.copyfileobj(infile, sys.stdout)
