import numpy as np
from functools import reduce
from operator import add

def read_csv(fn, sep = ';', ndim=2):
	""
	fd = open(fn)
	# ll = list(csv.reader(fd, delimiter=' '))
	ll = [[float(e.strip()) for e in line.split(sep)] for line in fd]
	fd.close()
	if ndim != 2:
		ll = reduce(add,ll,[])
	return ll

def trunc_sample(s):
	""
	#s = np.random.normal(loc=loc,scale=scale,size=size)
	if s.ndim == 1:
		k = 0
		k -= 1
		while s[k]<0: k -= 1 ## s[k] >= 0
		for i,x in enumerate(s):
			if x < 0:
				s[i] = s[k]
				k -= 1
				while s[k]<0: k -= 1 ## s[k] >= 0
	else:
		assert s.ndim >= 2
		for i,x in enumerate(s):
			trunc_sample(x)
	return s

def longevities2pop(l):
	"""
	l : array of life lengths (in years)
	"""
	mi = l.min()
	# assert mi >= 0, 'min'
	if mi >= 1:
		print('min strange: {}'.format(mi))
	ma = l.max()
	if ma <= 50:
		print('max strange: {}'.format(ma))
	m = int(np.floor(ma))+1
	# like hist
	deaths = np.zeros(m)
	l_size = 0
	for t in l:
		if t >= 0:
			deaths[int(np.floor(t))] += 1
			l_size += 1
	deaths_cumul = deaths.cumsum()
	assert deaths_cumul[-1] == l_size
	pop = l_size - np.hstack((0, deaths_cumul[:-1]))
	return pop, deaths

def longevities2lambda(l, sz_max=200):
	""
	pop, deaths = longevities2pop(l)
	hr = deaths/pop
	if sz_max and hr.size > sz_max:
		hr = hr[:sz_max]
	return hr
