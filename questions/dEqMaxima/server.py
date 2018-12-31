import sympy as sym
import scipy.optimize
from random import randint

x = sym.Symbol('x')
f = sym.Function('f')
initial_displacement = randint(0,9)
initial_velocity = randint(0,9)
correct_answer = "DNE"

# f"(x) - 3f'(x) + 2f(x) = 0
diffeq = f(x).diff(x,2) - 3 * f(x).diff(x) + 2*f(x)
#randomised starting displacment and initial velocity
conditions = {f(0): initial_displacement, f(x).diff(x).subs(x, 0): initial_velocity}
#finding f(x) with given initial conditions, using rhs as dsolve returns and equation
solution = sym.simplify(sym.dsolve(diffeq, f(x), ics = conditions)).rhs
#converting function to scipy compatible format
fun = sym.lambdify(x, solution, "numpy")

#finding maxima by finding the minimum of the negative of the function
max_x = scipy.optimize.fmin(lambda x: -fun(x), 0, full_output = True)
warnflag = max_x[4]
maxima = max_x[0]

if warnflag == 0 and maxima > 0:
    correct_answer = maxima

print(solution)
print(correct_answer)
