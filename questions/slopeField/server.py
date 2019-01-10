import numpy as np
import sympy as sym
from matplotlib import pyplot as plt
from io import BytesIO

option_coeffs = []
answer_coeffs = None

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

def file(data):
    if data['filename']=='answer.png':
        return plot(answer_coeffs)
    elif "option" in data['filename']:
        i = int(''.join(filter(str.isdigit, data['filename'])))
        return plot(option_coeffs[i])

def generate(data):
#generating answer plot
    answer_coeffs = randomize()

#defining a sympy expression for the question
#TODO clean this up and consolidate into one function
    x, y = sym.symbols('x y')
    question = answer_coeffs[0]*x**2 - answer_coeffs[1]*y**2
    
#generating other plots for options
    for i in range(3):
        coeffs = randomize()
        #avoiding identical options
        while(np.any(option_coeffs in answer_coeffs) or np.any(option_coeffs in coeffs)):
            coeffs = randomize()
        option_coeffs.append(coeffs)
   
    data["params"]["f"] = sym.latex(question)
return data
