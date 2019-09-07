from time import ctime

from torbjorn.version import VERSION


def run():
    cur_time = ctime()
    text = f"""
    # Torbjorn
    
    Version {VERSION} ({cur_time} +0800)
    """
    print(text)
