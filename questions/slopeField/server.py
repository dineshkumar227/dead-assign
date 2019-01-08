import numpy as np
import sympy as sym
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
#setting extent of graph and number of samples
    x = np.linspace(-1,1,15)
    y = np.linspace(-1,1,15)

    for j in x:
        for k in y:
            domain = np.linspace(j-0.07,j+0.07,2)
            slope = diff(j,k,coeffs)

            def fun(x1,y1):
                z = slope*(domain-x1)+y1
                return z

            plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')

    plt.grid(True)
    img = BytesIO()
    plt.savefig(img, bbox_inches='tight', format='png')

    return img

def generate(data):
#generating answer plot
    answer_coeffs = randomize()
    option_coeffs = []

#defining a sympy expression for the question
#TODO clean this up and consolidate into one function
    x, y = sym.symbols('x y')
    question = answer_coeffs[0]*x**2 - answer_coeffs[1]*y**2
    data["params"]["f"] = sym.latex(question)
    
#generating other plots for options
    for i in range(3):
        coeffs = randomize()
        #avoiding identical options
        while(answer_coeffs in option_coeffs or coeffs in option_coeffs):
            coeffs = randomize()
        option_coeffs.append(coeffs)

    
    def file(data):
        if data['filename']=='answer.png':
            return plot(answer_coeffs)
        else if data['filename']=='option.png':
            return plot(option_coeffs.pop())
return data
