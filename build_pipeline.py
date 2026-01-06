def build_pipeline(operation_names):
    if not isinstance(operation_names, list):
        raise TypeError("operation_names must be a list of strings.")

    for name in operation_names:
        if not isinstance(name, str):
            raise TypeError("operation_names must contain only strings.")

    def inc(x):
        return x + 1

    def double(x):
        return x * 2

    def triple(x):
        return x * 3

    def square(x):
        return x ** 2

    operations = {
        "inc": inc,
        "double": double,
        "triple": triple,
        "square": square,
    }

    for name in operation_names:
        if name not in operations:
            raise KeyError(f"Unknown operation name: {name}")

    def pipeline(x):
        for name in operation_names:
            x = operations[name](x)
        return x

    return pipeline
