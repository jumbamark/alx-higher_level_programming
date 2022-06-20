#!/usr/bin/python3


def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        result = None
    return result
