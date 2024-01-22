#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of two integers a and b."""
    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
