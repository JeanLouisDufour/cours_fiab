import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from operator import add
from math import log, pow

# from scipy.stats import gompertz

write_figs = False

def read_csv(fn, sep = ';', ndim=2):
	""
	fd = open(fn)
	# ll = list(csv.reader(fd, delimiter=' '))
	ll = [[float(e.strip()) for e in line.split(sep)] for line in fd]
	fd.close()
	if ndim != 2:
		ll = reduce(add,ll,[])
	return ll

def gompertz(lambda0, T2, ny = 100):
	""
	f = pow(2.0, 1.0/T2)
	Lambda = [lambda0]*ny
	for i in range(1,ny):
		Lambda[i] = f*Lambda[i-1]
	return Lambda

graunt = read_csv('table_graunt.csv')
print(graunt)

ulpian = read_csv('table_ulpian.csv')
print(ulpian)
x = [u[0] for u in ulpian]
y_ulp = [u[1] for u in ulpian]
y_cus = [u[2] for u in ulpian]
plt.plot(x, y_ulp, color='green', label='ulpian')
plt.plot(x, y_cus, color='blue' , label='customary')
plt.legend(loc='upper right') # obligatoire, et provoque l'affichage
#plt.show()
if write_figs:
	plt.savefig('fig_ulpian.png') ## ne pas faire show() avant [sinon videè]

plt.figure()
halley = read_csv('table_halley.csv', ndim=1)
assert len(halley) == 84 and sum(halley) == 34000-107
halley_7by7 = read_csv('table_halley_7by7.csv', ndim=1)
# le dernier nombre est le reliquat apres 84
assert halley_7by7[-1] == 107
for i in range(len(halley_7by7)-1):
	assert halley_7by7[i] == sum(halley[i*7:i*7+7])
assert sum(halley_7by7) == 34000
#
#halley_compl = [17,14,13,12,11,10,9,8,7,6,5,4,3,2,1,1,1]
#assert sum(halley_compl) == 107
l = np.array(halley)
d = l[:-1]-l[1:]
p = d / l[:-1]
plt.plot(p, color='green', label='halley')

tab = read_csv('table_deparcieux.csv', sep=None)
years = [l[0] for l in tab] # tab(:,1)';
l = np.array([l[-1] for l in tab]) # tab(:,5)';
d = l[:-1]-l[1:]
z = d / l[:-1]
plt.plot(z, color='blue', label='deparcieux')

fy = pow(z[90]/z[45], 1/45)
# fy**T2 == 2  =>  T2 = log(2)/log(fy)
T2_depar = log(2) / log(fy)
L0_depar = 2.5e-4
z1 = gompertz(L0_depar, T2_depar)
#plt.plot(z1)
Lm_depar = 6e-3
zth_depar = np.array(z1) + Lm_depar
plt.plot(zth_depar, linestyle=':')

l = np.array([l[1] for l in tab]) # tab(:,5)';
d = l[:-1]-l[1:]
z = d / l[:-1]
plt.plot(z, color='red', label='21ieme siecle')

plt.yscale('log')
plt.legend(loc='lower right')
"""
if nargin
    clf
    fi = 1;
    t = years(1:end-fi);
    l  = pop(1:end-fi);
    d = l(1:end-1)-l(2:end);
    z = d./l(1:end-1);
    semilogy(t(1:end-1),z)
    %%%% version interpolee entre 45 et 90 ans
    c = (z(90)/z(45))^(1/45)
    c^10
    zz1 = z(45)/(c^44);
    zz = zz1*(c.^(0:length(z)-1));
    hold on
    semilogy(t(1:end-1),zz)
    %%%% gompertz
    mu = 70;
    si = 14; % plus c'est petit, plus c'est penché
    zzz = evpdf(t,mu,si)./(1-evcdf(t,mu,si));
    semilogy(t(1:end-1),zzz(1:end-1))
end
"""
print('INED')
plt.figure()
tab = read_csv('table_INED_2002_2004.csv', sep=None)
years = [l[0] for l in tab]
# hommes
l = np.array([l[1] for l in tab])
d = l[:-1]-l[1:]
z = d / l[:-1]
plt.plot(z, color='blue', label='INED 2003 hommes')
#
fy = pow(z[90]/z[40], 1/50)
# fy**T2 == 2  =>  T2 = log(2)/log(fy)
T2 = log(2) / log(fy)
L0 = 5.5e-5
z1 = gompertz(L0, T2)
#plt.plot(z1)
Lm = 1e-5
zth = np.array(z1) + Lm
plt.plot(zth, color='blue', linestyle=':')
# femmes
l = np.array([l[4] for l in tab])
d = l[:-1]-l[1:]
z = d / l[:-1]
plt.plot(z, color='pink', label='INED 2003 femmes')
#
fy = pow(z[90]/z[40], 1/50)
# fy**T2 == 2  =>  T2 = log(2)/log(fy)
T2 = log(2) / log(fy)
L0 = 2.5e-5
z1 = gompertz(L0, T2)
#plt.plot(z1)
Lm = 1e-5
zth = np.array(z1) + Lm
plt.plot(zth, color='pink', linestyle=':')

plt.yscale('log')
plt.legend(loc='lower right')

