import numpy as np
import matplotlib.pyplot as plt

def read_csv(fn, sep = ';'):
	""
	fd = open(fn)
	# ll = list(csv.reader(fd, delimiter=' '))
	ll = [[int(e.strip()) for e in line.split(sep)] for line in fd]
	fd.close()
	return ll

graunt = read_csv('table_graunt.csv')
print(graunt)
ulpian = read_csv('table_ulpian.csv')
print(ulpian)
x = [u[0] for u in ulpian]
y_ulp = [u[1] for u in ulpian]
y_cus = [u[2] for u in ulpian]
plt.plot(x, y_ulp, color='green', label='ulpian')
plt.plot(x, y_cus, color='blue' , label='customary')
plt.legend(loc='upper right') # obligatoire
#plt.show()
plt.savefig('fig_ulpian.png') ## ne pas faire show() avant [sinon videè]
## f.savefig('output.png', dpi='figure')
# savefig("exercice_2.png",dpi=72)
