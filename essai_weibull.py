import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
#import truncnorm, weibull_min
from lifetimes import longevities2pop, longevities2lambda

"""
Domaines :
N, LN, Gu*    ->  GuM, Gum
E, Ga, Ra, Wm ->  GuM, Wm  avec pour min : E -> E
U             ->  WM,  Wm
WM            ->  WM,  Gum
"""
"""
numpy.random.weibull(a, size=None)   ## (-ln(U01))**(1/a)
a = 1 --> exponentielle
on peut multiplier par lambda ()
"""

wrv = st.weibull_min
small = 0.1
c = 10**np.linspace(-1,1,17)
c = 2**np.linspace(0,4,401)
ma = wrv.stats(c, moments='m')
plt.plot(c,ma)
plt.yscale('log')

plt.figure()

sample_sz = 100000

### rappel : l'exponentielle est parametree avec scale=MTBF
###     par contre weibull est parametre avec 

mtbf = 50
u01 = np.random.uniform(size = sample_sz)
w1 = -np.log(u01) ## a=1
death_times = mtbf*w1
mtbf_estim = np.mean(death_times)
mtbf_estim1 = np.std(death_times)
print('mtbf : {} --> {}'.format(mtbf, np.mean(death_times)))
#pars_fit = st.weibull_min.fit(death_times)
#print('weibull_min params of exp : {} --> {}'.format(mtbf, pars_fit))

pop, death_nbs = longevities2pop(death_times)
plt.plot((death_nbs/pop)[:4*mtbf])
plt.yscale('log')
plt.xscale('log')

w2 = w1**0.5
death_times = mtbf*w2
#plt.figure()
print('mtbf : {} --> {}'.format(mtbf, np.mean(death_times)))
pop, death_nbs = longevities2pop(death_times)
plt.plot((death_nbs/pop)[:4*mtbf])

w4 = w2**0.5
death_times = mtbf*w4
#plt.figure()
print('mtbf : {} --> {}'.format(mtbf, np.mean(death_times)))
pop, death_nbs = longevities2pop(death_times)
plt.plot((death_nbs/pop)[:4*mtbf])

w8 = w4**0.5
death_times = mtbf*w8
#plt.figure()
print('mtbf : {} --> {}'.format(mtbf, np.mean(death_times)))
pop, death_nbs = longevities2pop(death_times)
plt.plot((death_nbs/pop)[:4*mtbf])

w16 = w8**0.5
death_times = mtbf*w16
#plt.figure()
print('mtbf : {} --> {}'.format(mtbf, np.mean(death_times)))
pop, death_nbs = longevities2pop(death_times)
plt.plot((death_nbs/pop)[:4*mtbf])

