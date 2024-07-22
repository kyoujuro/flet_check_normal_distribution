import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.random.poisson(lam=3, size=1000)


observed_freq, bins = np.histogram(data, bins=range(0, max(data)+2))
expected_freq = [len(data) * stats.poisson.pmf(k, 3) for k in range(0, max(data)+1)]

expected_freq = np.array(expected_freq)
expected_freq *= observed_freq.sum() / expected_freq.sum()

chi2_stat, p_value = stats.chisquare(f_obs=observed_freq, f_exp=expected_freq)
if p_value > 0.05:
    print('データはポアソン分布に従っていると考えられます。')
else:
    print('データはポアソン分布に従っていないと考えられます。')


