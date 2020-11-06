from Calculator.Calculator import Calculator
from Statistics.Mean import mean1
from Statistics.Median import median1
from Statistics.Mode import mode1
from Statistics.Variance import variance_1
from Statistics.StandardDeviation import standard_deviation1
from Statistics.ZScore import z_score1


class Statistics(Calculator):

    def __init__(self):
        pass

    def mean(self, data):
        self.result = mean1(data)
        return self.result

    def median(self, data):
        return median1(data)

    def mode(self, data):
        return mode1(data)

    def variance(self, data):
        return variance_1(data)

    def standard_deviation(self, data):
        return standard_deviation1(data)

    def z_score(self, data):
        return z_score1(data)
