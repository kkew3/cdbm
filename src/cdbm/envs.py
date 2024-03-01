import os


def allow_record_counts():
    return os.environ.get('CDBM_RECORD_COUNT', '') == '1'


def get_editor():
    if 'CDBM_EDITOR' in os.environ:
        return os.environ['CDBM_EDITOR']
    if 'EDITOR' in os.environ:
        return os.environ['EDITOR']
    return 'vim'
