import signal
from logging import getLogger
from time import perf_counter
from functools import wraps, partial


default_logger = getLogger(__name__)


def run_time(func=None, *, logger=default_logger, name=None):
    if func is None:
        return partial(run_time, logger=logger, name=name)

    if name is None:
        name = func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        _return = func(*args, **kwargs)
        cost_time = round(perf_counter() - start_time, 5)
        logger.warning(f"[{name}] run time(s): {cost_time}")
        return _return

    return wrapper


def run_count(func=None, *, logger=default_logger, name=None):
    if func is None:
        return partial(run_count, logger=logger, name=name)

    if name is None:
        name = func.__name__

    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        logger.warning(f"[{name}] run count(t): {count}")
        return func(*args, **kwargs)
    return wrapper


def ctrl_c(func):
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def signal_handler(_a, _b):
    while True:
        exit_flag = input("Are you sure to quit? (yes|y) / (no|n)\n>> ")
        if exit_flag in {"yes", "y"}:
            default_logger.warning(">> exit...")
            exit()
        elif exit_flag in {"no", "n"}:
            break
