import numpy as np
from matplotlib import pyplot as plt
from io import BytesIO

# Differential equation
def diff(x,y,coeffs):
    return coeffs[0]*x**2 - coeffs[1]*y**2  # ax^2 - by^2

def randomize():
    #generate 2 random coefficients from -9 to 9 
    coeffs = np.random.random_integers(-9,9,2)

    #dont want 0's do we?
    if coeffs[0]==0:
        coeffs[0]=1
    if coeffs[1]==0:
        coeffs[1]=1
    return coeffs


#plots slope fields and returns a bitstream
def plot(coeffs):
    img = BytesIO()

    for j in x:
        for k in y:
            domain = np.linspace(j-0.07,j+0.07,2)
            slope = diff(j,k,coeffs)

            def fun(x1,y1):
                z = slope*(domain-x1)+y1
                return z

            plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')

    plt.grid(True)
    plt.show()
    plt.savefig(img, bbox_inches='tight')
    img.seek(0)

    return img

#setting extent of graph and number of samples
x = np.linspace(-1,1,15)
y = np.linspace(-1,1,15)

#generating answer plot
answer_coeffs = randomize()
answer_plot = plot(answer_coeffs)

option_plots = []

#generating other plots for options
for i in range(3):
    coeffs = randomize()
    print(coeffs)

    #avoiding identical options
    while(coeffs[0] == answer_coeffs[0]):
        coeffs = randomize()
    option_plots.append(plot(coeffs))

#TODO embed these png bitstreams as images in question html

print("End of the program")
