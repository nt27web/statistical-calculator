import unittest
from Statistics.PopulationSampler import PopulationSampler
import statistics
import scipy.stats as st


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.population_sampler = PopulationSampler()
        self.data = [0, 1, 2, 5, 9, 11, 34, 55, 23, 19, 78, 99, 15]

    # Simple random sampling
    def test_get_simple_random_sampling(self):
        self.assertEqual(len(self.population_sampler.get_simple_random_sampling(5, 5, 2, self.data)), 5)
        self.assertTrue(
            set(self.population_sampler.get_simple_random_sampling(5, 5, 2, self.data)).issubset(set(self.data)))

    # Confidence Interval For a Sample
    def test_get_confidence_interval(self):
        conf_interval = st.t.interval(alpha=0.95
                                , df=len(self.data) - 1
                                , loc=statistics.mean(self.data)
                                , scale=st.sem(self.data)
                              )
        ci = self.population_sampler.get_confidence_interval(self.data)

        #print("Confdence interval")
        #print(conf_interval)
        #print(ci)
        #self.assertTrue(set(conf_interval).issubset(ci))

    # Margin of Error
    def test_get_margin_of_error(self):
        q = 0.05 # assumption
        result = self.population_sampler.get_margin_of_error(self.data, q)

        sd = statistics.stdev(self.data)
        z = st.norm.ppf(1-(1-q)/2)
        se = sd / statistics.sqrt(len(self.data))
        moe = z * se
        #print("Margin of Error")
        #print(moe)
        #print(result)
        #self.assertTrue(result-moe >= 0.1)

    # Cochran’s Sample Size Formula
    def test_get_result_by_cochrans_sample_size(self):
        # n = 100000
        cl = 0.95
        e = 0.05
        p = 0.5
        #print(self.population_sampler.get_result_by_cochrans_sample_size(p, e, cl))

    # How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    """def test_get_sample_size_by_confidence_interval_and_width(self):
        print(self.population_sampler.get_sample_size_by_confidence_interval_and_width(self.data))"""


if __name__ == '__main__':
    unittest.main()
