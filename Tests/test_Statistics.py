import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
import pprint
import random
import statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = []
        for i in range(0, 10):
            num = random.randint(0, 15)
            self.testData.append(num)
        print(self.testData)
        self.mean_value = statistics.mean(self.testData)
        self.median_value = statistics.median(self.testData)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, self.mean_value)
    def test_median_calculator(self):
        median = self.statistics.median_1(self.testData)
        self.assertEqual(median, self.median_value)


if __name__ == '__main__':
    unittest.main()

