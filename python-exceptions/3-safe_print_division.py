#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a/b
        return result
    except Exception:
        return result
    finally:
        print("Inside result: {}".format(result))
