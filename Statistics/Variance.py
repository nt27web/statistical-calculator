from Statistics.Mean import mean1
from Calculator.Division import division
def variance_1(data):
    x1=mean1(data)
    num_values = len(data)
    total = 0
    total1 = 0
    data1=[]
    for i in data[0:]:
        a=data[i-1]
        total = (a-x1)**2
        data1.append(total)
    total1=sum(data1)
    return division(num_values,total1)