import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import truncnorm, weibull_min

from lifetimes import longevities2pop, longevities2lambda

sample_sz = 1000000

### rappel : l'exponentielle est parametree avec scale=MTBF
###     par contre weibull est parametre avec 

mtbf = 50
s50 = np.random.exponential(scale = 50, size = sample_sz)
s60 = np.random.exponential(scale = 100, size = sample_sz)
s = np.hstack((s50,s60))
s50_m = np.mean(s50)
print('mtbf of exp : {} --> {}'.format(50, s50_m))
#pars_fit = weibull_min.fit(death_times)
#print('weibull_min params of exp : {} --> {}'.format(mtbf, pars_fit))


l = longevities2lambda(s, sz_max = None)
plt.plot(l)
