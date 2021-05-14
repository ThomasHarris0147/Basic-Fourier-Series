import numpy as np
from matplotlib import pyplot as plt
from math import sin,cos,exp,pi,sqrt
import math

# the circular equation
def step(x):
    r = 1
    xx = (x%(2*r))
    return sqrt(r**2-(xx-r)**2)
# L is the period of the step function
# vectors is how many coffecients of a and b
# step is the function above
def fourier_transform(L,vectors,step): 
    def trapezoid_integration(f, a, b, n, level, L): # method of integration
        h = (b-a)/n
        return h/2* (f(a,level,L) + 2*sum(f(a+i*h,level,L) for i in range(1, n)) + f(b, level,L))
    def A_function(x,i,L): # a equation
        return step(x)*cos(i*x*pi/L)
    def B_function(x,i,L): # b equation
        return step(x)*sin(i*x*pi/L)
    a_b_range = [x for x in range(vectors)] # number of equations/vectors
    a = [trapezoid_integration(A_function,0,2*L,1000,i,L)*1/L for i in a_b_range] #computing A
    b = [trapezoid_integration(B_function,0,2*L,1000,i,L)*1/L for i in a_b_range] #computing B
    def y(x,L): # creating a function that repeats every period
        return a[0]/2 + sum([a[i]*cos(i*pi*x/L) for i in range(1, len(a_b_range))]) + sum([b[i]*sin(i*pi*x/L) for i in range(1, len(a_b_range))])
    #typical plotting of the function
    xs = np.linspace(0,5,1000)
    ys = [y(x,L) for x in xs]
    yys = [step(xx) for xx in xs]
    plt.plot(xs,yys)
    plt.plot(xs,ys)
    plt.show()

fourier_transform(2,1,step)
fourier_transform(2,5,step)
fourier_transform(2,10,step)
fourier_transform(2,30,step)
fourier_transform(2,100,step)
