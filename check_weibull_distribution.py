import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


data = np.random.weibull(a=1.5, size=1000)
shape, loc, scale = stats.weibull_min.fit(data, floc=0)
d_stat, p_value = stats.kstest(data, 'weibull_min', args=(shape, loc, scale))

if p_value > 0.05:
    print('データはワイブル分布に従っていると考えられます。')
else:
    print('データはワイブル分布に従っていないと考えられます。')

