import numpy as np
import matplotlib.pyplot as plt

from lifetimes import longevities2pop, longevities2lambda, trunc_sample

#a = np.random.choice((-1,1), size=(3,3)) # weibull

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

numpy.random.gumbel(loc=0.0, scale=1.0, size=None)
mean = m + 0.57721 b,  var = (pi**2/6)*b**2   -->  max-gumbel  (min : -)
verifier que m (loc) = mode
"""

sample_sz = 100000

print('expo mtbf=50')
plt.figure()
mtbf = 50
death_times = np.random.exponential(scale = mtbf, size = sample_sz) ### mtbf = 50 unites
pop, death_nbs = longevities2pop(death_times)
plt.plot((death_nbs/pop)[:4*mtbf])

print('min de 2 expos 50 / 100 --> 30')
plt.figure()
mtbf2 = 100
death_times2 = np.random.exponential(scale = mtbf2, size = sample_sz) ### mtbf = 50 unites
death_times = np.vstack((death_times, death_times2)).min(axis=0)
assert death_times.size == sample_sz
pop, death_nbs = longevities2pop(death_times)
plt.plot((death_nbs/pop)[:4*mtbf])
plt.title('min de 2 expos 50 / 100 --> 30')

###############################################



title = 'lambda of min-uniform-0-100'
print(title)
plt.figure()
death_times = np.random.uniform(low=0, high=100, size = sample_sz)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.uniform(low=0, high=150, size = (2,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.uniform(low=0, high=250, size = (4,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.uniform(low=0, high=450, size = (8,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.uniform(low=0, high=850, size = (16,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))

plt.yscale('log')
plt.title(title)

###################################"

title = 'lambda of min-lognormal-0-100'
print(title)
plt.figure()
# mean (log (sample_lognormal(m,s))) == m
##   ce qui ne veut pas dire que mean(sample_lognormal(m,s)) == exp(m)
##   ici les valeurs de m sont choisies pour que mean(sample_lognormal_min) == 50
# std (log (sample_lognormal(m,s))) == s
death_times = np.random.lognormal(mean=3.413, sigma=1, size = sample_sz)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.lognormal(mean=4.146, sigma=1, size = (2,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.lognormal(mean=4.710, sigma=1, size = (4,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.lognormal(mean=5.163, sigma=1, size = (8,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = np.random.lognormal(mean=5.543, sigma=1, size = (16,sample_sz)).min(axis=0)
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
plt.yscale('log')
plt.title(title)

###############################################

title = 'lambda of min normale'
print(title)
plt.figure()
# scale == std
sampler = np.random.normal
tr = trunc_sample
death_times = tr(sampler(loc=50, scale=15, size = sample_sz))
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = tr(sampler(loc=58, scale=15, size = (2,sample_sz)).min(axis=0))
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = tr(sampler(loc=65, scale=15, size = (4,sample_sz)).min(axis=0))
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = tr(sampler(loc=72, scale=15, size = (8,sample_sz)).min(axis=0))
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
death_times = tr(sampler(loc=77, scale=15, size = (16,sample_sz)).min(axis=0))
print(np.mean(death_times)); plt.plot(longevities2lambda(death_times))
plt.yscale('log')
plt.title(title)

assert False

plt.figure()

death_times = np.random.gumbel(loc = 45.0, scale = 10.0, size = 10000)
pop, death_nbs = longevities2pop(death_times)
plt.plot(death_nbs/pop)


assert False

#a = np.random.Generator.normal(size=(2,2))
#a = np.random.default_rng().normal(size=(2,2))
data = np.random.normal(size=1000)

hx,hy,_ = plt.hist(data, bins=10, density=1)

# 
data = np.random.normal(size=(1000,1000))
data1 = np.amin(data, axis=0)
plt.figure()
hx,hy,_ = plt.hist(data1, bins=10, density=1, label='min of 1000 normals')
plt.legend(loc='upper left')

#
sample_sz = 1000
samples_nb = 1000
#data = np.random.uniform(size=(samples_nb,sample_sz))
data = np.random.uniform(size=(samples_nb,sample_sz))
means = []
for n in range(1,samples_nb+1):
	### on ne prend que les n premieres lignes
	### et on fait le min de chaque colonne
	data1 = data[:n,:].min(axis=0)
	assert data1.shape == (sample_sz,)
	means.append(data1.mean())
plt.figure()
plt.plot(range(1,samples_nb+1),means)
#hx,hy,_ = plt.hist(data1, bins=10, label='min of 1000 uniforms')
#plt.legend(loc='upper left')
