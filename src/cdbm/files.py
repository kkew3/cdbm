from pathlib import Path


def get_config_dir():
    config_dir = Path.home() / '.config' / 'cdbm'
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def get_config_file():
    return get_config_dir() / 'cdbm'


def get_count_file():
    return get_config_dir() / 'count'
