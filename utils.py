from functools import wraps

__author__ = 'Darryl'
__date__ = '3-11-2014'


def convert_boolean_to_binary(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return 1
        else:
            return 0

    return decorator


def accept_binary_only(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            result = int(result)
        except ValueError:
            print("Incorrect input: not an int: got %s" % result)
            result = func(*args, **kwargs)

        if result not in (0, 1):
            print("Incorrect input: not 1 or 0: got %s" % result)
            result = func(*args, **kwargs)
        return result

    return decorator


def profiled(func):
    called = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal called
        called += 1
        return func(*args, **kwargs)

    wrapper.called = lambda: called
    return wrapper