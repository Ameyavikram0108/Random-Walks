from scipy.integrate import dblquad
from math import cos, sin, pi, sqrt

def integrand(n1, n2, k1, k2, t):
    p1 = cos(n1*k1)*cos(n2*k2)
    p2 = 3 / sqrt(1 + 4*((cos(k1)**2)) + 4*(cos(k1)*cos(k2)))
    p3 = -p2

    return p1*((p2**t) + (p3**t))

#even t
print(dblquad(lambda y, x: integrand(1,1,x,y,10), -pi, pi, lambda x: -pi, lambda x: pi)[0] / (2*(pi**2)))
#odd t
print(dblquad(lambda y, x: integrand(1,1,x,y,11), -pi, pi, lambda x: -pi, lambda x: pi)[0] / (2*(pi**2)))
