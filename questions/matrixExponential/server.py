import numpy as np
import sympy as sym
import prairielearn as pl
from sympy import *

def generate(data):
#range of allowed values, dont want this to be too big to avoid cubersome problems
    nMin = 0
    nMax = 1
#dimensions of matrix
    matrixRows = matrixCols = 3

#generating a random matrix
#matrix2 = sym.Matrix(np.random.random_integers(nMin, nMax, (3,3)))
#TODO randomisation creating complex cases, talk to Bronski about math behind this
    A = np.array([[2, 0, 1],
                   [0, 1, 1],
                   [0, 1, 1]])
    data["params"]["A"] = pl.to_json(A)
#TODO Make this more elegant
    E = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    data["params"]["E"] = pl.to_json(E)

    matrix = sym.Matrix(A)
    t = sym.Symbol('t')
    matrix_exp = sym.simplify(sym.exp(matrix * t))
    for i in range(len(matrix_exp)):
        ans_name = "m" + str(i)
        data["correct_answers"][ans_name] = pl.to_json(matrix_exp[i])

    return data
'''
TODO: Something is wrong with my math here, check with Bronski

c1,c2,c3 = sym.symbols(('c0:3'))
x0 = sym.Symbol('x0')#sym.Matrix([c1,c2,c3]).T
B = sym.Matrix([0, 0, sym.exp(-2*t)]).T

x = sym.Function('x')
s = sym.Symbol('s')

print(x0)

integration = sym.integrate(exp((t-s)*A)*exp(-2*s), (s, 0, t))

print(sym.simplify(integration))

solution = sym.Eq(x(t), matrix_exp * x0 + integration)

print(solution)
'''
