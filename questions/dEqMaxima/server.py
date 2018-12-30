import sympy as sym
from random import randint

x = sym.Symbol('x')
f = sym.Function('f')
initial_velocity = randint(1,9)

diffeq = sym.Eq(f(x).diff(x,2), 3 * f(x).diff(x) - 2*f(x))
conditions = {f(0):2, f(x).diff(x).subs(x, 0): initial_velocity}

print(sym.simplify(sym.dsolve(diffeq, f(x), ics = conditions)))

