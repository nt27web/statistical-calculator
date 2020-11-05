from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median1
from Statistics.Mode import mode1

class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median_1(self, data):
        print(median1(data))

    def mode(self, data):
        print(mode1(data))
    