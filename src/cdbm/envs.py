import os


def allow_record_counts():
    return os.environ.get('CDBM_RECORD_COUNT', '') == '1'
