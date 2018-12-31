import sympy as sym
import scipy.optimize
from random import randint

x = sym.Symbol('x')
f = sym.Function('f')
initial_displacement = randint(0,9)
initial_velocity = randint(0,9)
correct_answer = "DNE"

diffeq = f(x).diff(x,2) - 3 * f(x).diff(x) + 2*f(x)
conditions = {f(0): initial_displacement, f(x).diff(x).subs(x, 0): initial_velocity}
solution = sym.simplify(sym.dsolve(diffeq, f(x), ics = conditions)).rhs

fun = sym.lambdify(x, solution, "numpy")

max_x = scipy.optimize.fmin(lambda x: -fun(x), 0, full_output = True)
warnflag = max_x[4]
maxima = max_x[0]

if warnflag == 0 and maxima > 0:
    correct_answer = maxima
print(solution)
print(correct_answer)

#print(sym.solve(solution.diff(x), x))
#print(solution.diff(x))
