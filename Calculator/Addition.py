def addition(a, b):
    if (isinstance(a, float) and isinstance(b, float)) or (isinstance(a, float) and isinstance(b, int)) or (isinstance(a, int) and isinstance(b, float)):
        return float(a) + float(b)
    elif isinstance(a, int) and isinstance(b, int):
        return int(a) + int(b)
    else:
        raise Exception("Data type not supported for addition operation!")

