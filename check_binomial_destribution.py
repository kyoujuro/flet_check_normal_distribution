import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

n, p = 10, 0.5  
data = np.random.binomial(n, p, size=1000)

observed_freq, bins = np.histogram(data, bins=range(0, n+2))
expected_freq = [len(data) * stats.binom.pmf(k, n, p) for k in range(0, n+1)]

expected_freq = np.array(expected_freq)
expected_freq *= observed_freq.sum() / expected_freq.sum()

chi2_stat, p_value = stats.chisquare(f_obs=observed_freq, f_exp=expected_freq)

if p_value > 0.05:
    print('データは二項分布に従っていると考えられます。')
else:
    print('データは二項分布に従っていないと考えられます。')
