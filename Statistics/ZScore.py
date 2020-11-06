from Calculator.Subtraction import subtraction
from Calculator.Division import division_float
from Statistics.Mean import mean1
from Statistics.StandardDeviation import standard_deviation1
def z_score1(data):
    value_mean=mean1(data)
    z=[]
    for i in range(0,len(data)):
        a=subtraction(value_mean,data[i])
        b=division_float(standard_deviation1(data),a)
        z.append(b)
    return z