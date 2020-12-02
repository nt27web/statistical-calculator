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

        st1_degree_of_freedom = self.stats.subtract(len(data), 1)
        st2_alpha = self.stats.divide(2, self.stats.subtract(1, 0.95))
        st3 = st.t.ppf(1 - st2_alpha, df=st1_degree_of_freedom)
        st4 = self.stats.divide(self.stats.square_root(len(data)), self.stats.stats_standard_deviation(data))
        st5 = self.stats.multiply(st3, st4)
        st6 = self.stats.subtract(self.stats.stats_mean(data), st5)
        st7 = self.stats.add(self.stats.stats_mean(data), st5)

        conf_interval = [st6, st7]
        return conf_interval

        # Margin of Error
    def get_margin_of_error(self, data, q):
        st1_z_critical_score = st.norm.ppf(1 - (1 - q) / 2)
        st2_sd = self.stats.stats_standard_deviation(data)
        #st3 = self.stats.multiply(st1_z_critical_score, st2_sd)
        se = self.stats.divide(self.stats.square_root(len(data)), st2_sd)
        margin_of_error = self.stats.multiply(st1_z_critical_score, se)

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
        za_2 = st.norm.ppf(1 - (1 - cl) / 2)
        print("za2 - " + str(za_2))
        e = 0.5
        print("e - " + e)
        p = 0.5
        q = 1 - p
        # step 2
        s2 = self.stats.multiply(p, q)
        print("s2 - " + s2)
        # step 3
        s3 = self.stats.divide(za_2, e)
        print("s3 - " + s3)
        # step 4
        s4 = self.stats.square(s3)
        print("s4 - " + s4)
        # step 5 ( final )
        s5 = self.stats.multiply(s2, s4)
        print("s5 - " + s5)
        # this is the sample population size for an unknown population standard deviation
        return s5

