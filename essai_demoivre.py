import numpy as np
import matplotlib.pyplot as plt
import lifetimes

#hal = np.loadtxt('table_halley.csv', delimiter = ';')
hal = np.array(lifetimes.read_csv('table_halley.csv', ndim=1))
print(hal)

### la valeur presente d'une annuite de 100 (interet a 5%) est 95.23
print(100/1.05)
### 95.238..., donc il arrondit au centieme INFERIEUR

### valeur de la 'first year RENT' : 93.80
print(95.23 * 523/531)
### 93.7952..., donc ici il arrondit au centieme SUPERIEUR
assert hal[29] == 531
sz = hal.size - 30
rents = 100/ np.power(1.05, np.arange(1,sz+1))
values = (rents * hal[30:])/hal[29] 
value = sum(values)  ### environ 1300

plt.plot(hal)
plt.plot(-np.diff(hal))
