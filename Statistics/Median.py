from Calculator.Division import division
from Calculator.Addition import addition
def median1(data):
    num_values = len(data)
    if((num_values%2)==0):
        value=int(division(2,num_values))
        a=data[value]
        value=value-1
        b=data[value]
        c=addition(b,a)
        d=division(2,c)
        return(d)
    else:
         value=int(division(2,num_values))
         e=data[value]
         return(e)