import numpy as np
import sympy as sym
from sympy import *

#range of allowed values, dont want this to be too big to avoid cubersome problems
nMin = 0
nMax = 1
#dimensions of matrix
matrixRows = matrixCols = 3

#generating a random matrix
#matrix2 = sym.Matrix(np.random.random_integers(nMin, nMax, (3,3)))
#TODO randomisation creating complex cases, talk to Bronski about math behind this
A = matrix = sym.Matrix([[2, 0, 1],
                         [0, 1, 1],
                         [0, 1, 1]])

t = sym.Symbol('t')

matrix_exp = sym.simplify(sym.exp(matrix * t))
print(matrix_exp)

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
