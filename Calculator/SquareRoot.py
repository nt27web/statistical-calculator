import math


def square_root(a):
    if isinstance(a, float):
        return round(math.sqrt(float(a)), 9)
    elif isinstance(a, int):
        return round(math.sqrt(a), 9)
    else:
        raise Exception("Data type not supported for square root operation!")

