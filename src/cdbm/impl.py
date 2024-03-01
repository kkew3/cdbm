import json
from pathlib import Path
import sys
import shutil
from dataclasses import dataclass
import subprocess
import logging

from cdbm import files
from cdbm import envs


@dataclass
class BookmarkEntry:
    key: str
    path: Path


def select_path(key: str):
    """
    Print the corresponding path and return ``True`` if ``key`` is found.
    """
    cdbm_file = files.get_config_file()
    found = None
    try:
        with open(cdbm_file, encoding='utf-8') as infile:
            for line in infile:
                line = line.rstrip('\n')
                # skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                tokens = line.split(maxsplit=1)
                # skip malformed lines
                if len(tokens) != 2:
                    continue
                if key == tokens[0]:
                    found = Path(tokens[1])
                    break
    except FileNotFoundError:
        logging.error('cdbm file is empty!')
        return False
    if not found:
        logging.error('key "%s" not found', key)
        return False
    print(found, end='')
    return True


def increment_count_file(key: str):
    """Will do nothing if count file is not allowed."""
    if not envs.allow_record_counts():
        return

    count_file = files.get_count_file()
    try:
        with open(count_file, encoding='utf-8') as infile:
            counts = json.load(infile)
    except FileNotFoundError:
        counts = {}
    counts[key] = counts.get(key, 0) + 1
    with open(count_file, 'w', encoding='utf-8') as outfile:
        json.dump(counts, count_file, indent=2)


def print_count_file():
    """Pretty-print the count file."""
    count_file = files.get_count_file()
    try:
        with open(count_file, encoding='utf-8') as infile:
            counts = list(json.load(count_file).items())
    except FileNotFoundError:
        counts = []
    if not counts:
        return
    # sort by the counts
    counts.sort(key=lambda x: x[1], reverse=True)
    counts = [(key, str(c)) for key, c in counts]
    max_width_count_str = max(len(c) for _, c in counts)
    for key, c in counts:
        print('{} {}'.format(c.rjust(max_width_count_str), key))


def print_config_file():
    """Pretty-print the cdbm configuration file."""
    # if not in tty, print as fast as possible without pretty-printing
    cdbm_file = files.get_config_file()
    if not sys.stdout.isatty():
        try:
            with open(cdbm_file, 'rb') as infile:
                shutil.copyfileobj(infile, sys.stdout.buffer)
        except FileNotFoundError:
            pass
        return

    COMMENT = '\033[90m'  # gray
    KEY = '\033[1;31m'  # bold red
    ERROR = '\033[31;43m'  # red with background yellow
    RESET = '\033[0m'
    try:
        with open(cdbm_file, encoding='utf-8') as infile:
            max_width_key = 0
            for line in infile:
                line = line.rstrip('\n')
                if not line:
                    continue
                if line.startswith('#'):
                    continue
                tokens = line.split(maxsplit=1)
                if len(tokens) == 2:
                    max_width_key = max(max_width_key, len(tokens[0]))
            infile.seek(0)
            for line in infile:
                line = line.rstrip('\n')
                if not line:
                    print()
                elif line.startswith('#'):
                    print(f'{COMMENT}{line}{RESET}')
                else:
                    tokens = line.split(maxsplit=1)
                    if len(tokens) != 2:
                        # must be 1
                        print(f'{ERROR}{line}{RESET}')
                    else:
                        key, path = tokens
                        key = key.ljust(max_width_key)
                        path = Path(path)
                        print(f'{KEY}{key}{RESET} {path}')
    except FileNotFoundError:
        pass


def post_edit_actions():
    _delete_absent_keys_from_count_file()


def _delete_absent_keys_from_count_file():
    """Will do nothing if count file is not allowed."""
    if not envs.allow_record_counts():
        return

    cdbm_file = files.get_config_file()
    # this will not include the keys in commented lines
    present_keys = set()
    try:
        with open(cdbm_file, encoding='utf-8') as infile:
            for line in infile:
                line = line.rstrip('\n')
                # skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                tokens = line.split(maxsplit=1)
                # skip malformed lines
                if len(tokens) != 2:
                    continue
                present_keys.add(tokens[0])
    except FileNotFoundError:
        pass

    count_file = files.get_count_file()
    try:
        with open(count_file, encoding='utf-8') as infile:
            counts = json.load(infile)
    except FileNotFoundError:
        # nothing to delete
        return

    keys_to_del = set(counts) - present_keys
    for key in keys_to_del:
        del counts[key]
    with open(count_file, 'w', encoding='utf-8') as outfile:
        json.dump(counts, outfile, indent=2)


def print_help():
    print('''\
cdbm [OPTION | <QUERY>]

OPTION (mutually exclusive)

    -h          print this message and exit
    -l          print the bookmark definitions
    -c          print the access counts of each bookmarked directory
    -e          edit the bookmark definition file''')


def edit_config_file():
    cdbm_file = files.get_config_file()
    editor = envs.get_editor()
    subprocess.run([editor, str(cdbm_file)])
