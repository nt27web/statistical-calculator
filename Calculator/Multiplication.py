def multiplication(a, b):
    if (isinstance(a, float) and isinstance(b, float)) or (isinstance(a, float) and isinstance(b, int)) or (
            isinstance(a, int) and isinstance(b, float)):
        return round(float(a) * float(b), 9)
    elif isinstance(a, int) and isinstance(b, int):
        return int(a) * int(b)
    else:
        raise Exception("Data type not supported for multiplication operation!")

