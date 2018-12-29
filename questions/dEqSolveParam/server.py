import sympy as sy
from random import randint

x = sy.symbols('x')
f = sy.Function('f')
diffeq = sy.Eq(f(x).diff(x,x) + f(x), sy.sec(x))
print("Solving: ")
print(sy.simplify(diffeq))
print(sy.simplify(sy.dsolve(diffeq, f(x), hint = 'nth_linear_constant_coeff_variation_of_parameters')))
