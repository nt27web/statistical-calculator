def square(a):
    if isinstance(a, float):
        return round(float(a) * float(a), 9)
    elif isinstance(a, int):
        return int(a) * int(a)
    else:
        raise Exception("Data type not supported for square operation!")