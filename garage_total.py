from math import pi, log
E0 = complex(0.0037586074608577866,-0.001597380074239428)
E1 = complex(-0.0005531026700240645, -0.00046163800083712014)
E2 = complex(-0.0006696859623934064, 0.00016886463123019858)
E3 = complex(0.27250450078371585, -4.5354372004478) * 10**(-4)
E4 = complex(0.5213097827398439, 0.6080424436132617)*10**(-4)
Etotal = E0 + E1 + E2 + E3 + E4
print("Champ total = " + str(Etotal))

f = 868.3* 10**6
w = 2 * pi * f
c = 299792458
L = c/f
he = L/(pi)
puissance = (he*abs(Etotal))**2
puissance = puissance / (8 * 73)
print("Puissance perçue = " + str(puissance))

dBm = 10 * log(puissance/(10**(-3)), 10)
print('dBm = ' + str(dBm))