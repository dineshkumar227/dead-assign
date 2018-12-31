import sympy as sy
from random import randint

x = sy.symbols('x')
f = sy.Function('f')

diffeq = sy.Eq(f(x).diff(x) - randint(1, 9)*f(x), randint(1,9)*x)

print("Solving: ")
print(sy.simplify(diffeq))
print(sy.simplify(sy.dsolve(diffeq, f(x))))

