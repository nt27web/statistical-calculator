def subtraction(a, b):
    if (isinstance(a, float) and isinstance(b, float)) or (isinstance(a, float) and isinstance(b, int)) or (
            isinstance(a, int) and isinstance(b, float)):
        return float(b) - float(a)
    elif isinstance(a, int) and isinstance(b, int):
        return int(b) - int(a)
    else:
        raise Exception("Data type not supported for subtraction operation!")
