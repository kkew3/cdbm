import sys
import shutil

if sys.platform == 'win32':
    import colorama
    try:
        colorama.just_fix_windows_console()
    except AttributeError:
        colorama.init()

cdbm_file = sys.argv[1]

if sys.stdout.isatty():
    GRAY = '\033[90m'
    BRIGHT_RED = '\033[1;31m'
    RST = '\033[0m'
    with open(cdbm_file, encoding='utf-8') as infile:
        key_width = 0
        for line in infile:
            if not line.startswith('#'):
                key_width = max(key_width, len(line.split(maxsplit=1)[0]))
        infile.seek(0)
        for line in infile:
            if line.startswith('#'):
                sys.stdout.write('{}{}{}'.format(GRAY, line, RST))
            else:
                tokens = line.split(maxsplit=1)
                sys.stdout.write('{}{}{} {}'.format(
                    BRIGHT_RED, tokens[0].ljust(key_width), RST,
                    ''.join(tokens[1:]) or '\n'))
else:
    with open(cdbm_file, encoding='utf-8') as infile:
        shutil.copyfileobj(infile, sys.stdout)
