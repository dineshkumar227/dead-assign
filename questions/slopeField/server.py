import numpy as np
from matplotlib import pyplot as plt

# Differential equation
# diff = y'= y/x (or say x+y)
def diff(x,y,coeffs):
    return coeffs[0]*x**2 - coeffs[1]*y**2  # ax^2 - by^2


x = np.linspace(-1,1,15)
y = np.linspace(-1,1,15)

#generate 2 random coefficients from -9 to 9 
coeffs = np.random.random_integers(-9,9,2)
if coeffs[0]==0:
    coeffs[0]=1

# use x,y
for j in x:
    for k in y:
        slope = diff(j,k,coeffs)
        domain = np.linspace(j-0.07,j+0.07,2)
        def fun(x1,y1):
            z = slope*(domain-x1)+y1
            return z
        plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')

plt.grid(True)
plt.show()
#plt.savefig('foo.png', bbox_inches='tight')
    
print("End of the program")
