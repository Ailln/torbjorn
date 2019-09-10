import functools
from datetime import datetime


def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        _return = func(*args, **kwargs)
        end_time = datetime.now()
        print(f">> [{func.__name__}] run time: {end_time - start_time}")
        return _return

    return wrapper


def run_count(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f">> [{func.__name__}] run count: {count}")
        return func(*args, **kwargs)

    return wrapper
