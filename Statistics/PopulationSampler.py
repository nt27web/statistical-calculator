from Statistics.RandomGenerator import RandomGenerator
from Statistics.Statistics import Statistics

import scipy.stats as st


class PopulationSampler(RandomGenerator):

    def __init__(self):
        self.stats = Statistics()
        pass

    # Simple random sampling
    def get_simple_random_sampling(self, size, seed, version, data):
        return self.get_rand_num_list_w_seed(size, seed, version, data)

    # Confidence Interval For a Sample
    def get_confidence_interval(self, data):

        conf_interval = st.t.interval(alpha=0.95
                        , df=len(data) - 1
                        , loc=self.stats.stats_mean(data)
                        , scale=st.sem(data)
                      )
        return conf_interval

        # Margin of Error
    def get_margin_of_error(self, data, cl):

        sd = self.stats.stats_standard_deviation(data)
        z_score = st.norm.ppf(1-(1-cl)/2)
        se = self.stats.divide(self.stats.square_root(len(data)), sd)
        margin_of_error = self.stats.multiply(z_score, se)

        return margin_of_error

    # Cochran’s Sample Size Formula
    def get_result_by_cochrans_sample_size(self, p, e, cl):
        z = st.norm.ppf(1-(1-cl)/2)
        print(self.stats.multiply(self.stats.multiply(self.stats.square(z), p), self.stats.square(e)))

        n = self.stats.multiply(self.stats.multiply(self.stats.square(z), p), self.stats.square(e))/(1-p)
        print(n)
        return round(n)

    # How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    def get_sample_size_by_confidence_interval_and_width(self, data):
        # step 1
        cl = 0.95
        za_2 = st.norm.ppf(1-(1-cl)/2)
        e = 0.5
        p = 0.5
        q = 1-p
        # step 2
        s2 = self.stats.multiply(p, q)
        # step 3
        s3 = self.stats.divide(za_2, e)
        # step 4
        s4 = self.stats.square(s3)
        # step 5 ( final )
        s5 = self.stats.multiply(s2, s4)
        # this is the sample population size for an unknown population standard deviation
        return s5

