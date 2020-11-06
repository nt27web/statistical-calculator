import unittest
from Statistics.PopulationSampler import PopulationSampler


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.population_sampler = PopulationSampler()
        self.data = [0, 1, 2, 5, 9, 11, 34, 55, 23, 19, 78, 99, 15]

    # Simple random sampling
    def test_get_simple_random_sampling(self):
        print(self.population_sampler.get_simple_random_sampling(5, 5, 2, self.data))

    # Confidence Interval For a Sample
    def test_get_confidence_interval(self):
        print(self.population_sampler.get_confidence_interval(self.data))

    # Margin of Error
    def test_get_margin_of_error(self):
        print(self.population_sampler.get_margin_of_error(self.data))

    # Cochran’s Sample Size Formula
    def test_get_result_by_cochrans_sample_size(self):
        p1 = 0
        p_diff = 0.5
        alpha = 0

        print(self.population_sampler.get_result_by_cochrans_sample_size(p1, p_diff, alpha))

    # How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    def test_get_sample_size_by_confidence_interval_and_width(self):
        print(self.population_sampler.get_sample_size_by_confidence_interval_and_width(self.data))


if __name__ == '__main__':
    unittest.main()
