from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Statistics.Mean import get_mean
from Statistics.StandardDeviation import get_standard_deviation


def get_z_score(data):
    if isinstance(data, float):
        data = [data]
    value_mean = get_mean(data)
    z = []
    for i in range(0, len(data)):
        a = subtraction(value_mean, data[i])
        b = division(get_standard_deviation(data), a)
        z.append(b)
    return z
