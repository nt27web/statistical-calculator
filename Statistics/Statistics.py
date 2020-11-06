from Calculator.Calculator import Calculator
from Statistics.Mean import mean1
from Statistics.Median import median1
from Statistics.Mode import mode1
from Statistics.Variance import variance_1
from Statistics.StandardDeviation import standard_deviation1


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean1(data)
        return self.result

    def median(self, data):
        return median1(data)

    def mode(self, data):
        print(mode1(data))

    def variance(self, data):
        print(variance_1(data))

    def standard_deviation(self, data):
        print(standard_deviation1(data))
