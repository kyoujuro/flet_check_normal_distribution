import unittest
import numpy as np
import check_binomial_distriburion

class DistributionTest(unittest.TestCase):
    def test_binomial_distribution(self):
        try:
            n, p = 10, 0.5
            data = np.random.binomial(n, p, size=1000)
            chi2_stat, p_value = check_binomial_distriburion(data, n, p)
            self.assertGreater(p_value, 0.05)
        except Exception as e:
            print(f'Error {e}')
    
    def test_poisson_distribution(self):
        try:
            data = np.random.poisson(lam=3, size=1000)
            chi2_stat, p_value = poisson_test(data, lam=3)
            self.assertGreater(p_value, 0.05)
        except Exception as e:
            print(f'Error {e}')



if __name__ == '__main__':
    unittest.main()
