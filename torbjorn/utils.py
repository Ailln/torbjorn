from datetime import datetime


def run_time(func):
    def wrapper(*args, **kw):
        start_time = datetime.now()
        func(*args, **kw)
        end_time = datetime.now()
        delta_time = end_time - start_time
        print(f">> function \"{func.__name__}\" cost time: {delta_time}")
    return wrapper
