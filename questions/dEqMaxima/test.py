import sympy as sym
import scipy.optimize
from random import randint

x = sym.Symbol('x')
f = sym.Function('f')
initial_displacement = randint(0,9)
initial_velocity = randint(0,9)
answer = "DNE"

# f"(x) - 3f'(x) + 2f(x) = 0
diffeq = f(x).diff(x,2) - 3 * f(x).diff(x) + 2*f(x)
#randomised starting displacment and initial velocity
conditions = {f(0): initial_displacement, f(x).diff(x).subs(x, 0): initial_velocity}
#finding f(x) with given initial conditions, using rhs as dsolve returns and equation
solution = sym.dsolve(diffeq, f(x), ics = conditions).rhs
#converting function to scipy compatible format
fun = sym.lambdify(x, solution, modules = ["numpy"])

#finding maxima by finding the minimum of the negative of the function
optimize_output = scipy.optimize.minimize(lambda x: -fun(x), 0)#, full_output = True, disp = False)
import code; code.interact(local=dict(globals(), **locals()))

if optimize_output.success == True and optimize_output.x[0] > 0: 
    answer = str(optimize_output.x[0])
print(answer)
