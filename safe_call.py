def safe_call(func, a, b):
    try:
        result = func(a, b)
        return (True, result, None)

    except (ZeroDivisionError,
            TypeError,
            ValueError,
            IndexError,
            KeyError) as e:
        return (False, None, e.__class__.__name__)

