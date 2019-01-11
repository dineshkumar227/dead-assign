import sympy as sym
import numpy
import scipy.optimize
from random import randint
import warnings


def generate(data):
    x = sym.Symbol('x')
    y = sym.Function('y')
    initial_displacement = randint(0,9)
    initial_velocity = randint(0,9)
    answer = "DNE"

    # y"(x) + 3y'(x) + 2y(x) = 0
    diffeq = y(x).diff(x,2) + 3 * y(x).diff(x) + 2*y(x)
    #randomised starting displacment and initial velocity
    conditions = {y(0): initial_displacement, y(x).diff(x).subs(x, 0): initial_velocity}
    #finding y(x) with given initial conditions, using rhs as dsolve returns and equation
    solution = sym.simplify(sym.dsolve(diffeq, y(x), ics = conditions)).rhs
    #converting function to scipy compatible format
    fun = sym.lambdify(x, solution, "numpy")

    #finding maxima by finding the minimum of the negative of the function
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        optimize_output = scipy.optimize.basinhopping(lambda x: -fun(x), 0, disp = False)
    maxima = optimize_output.x[0]

    if optimize_output.lowest_optimization_result.success == True and maxima > 0:
        answer = str(round(fun(maxima), 2))
        if len(answer) <= 3:
            answer = answer + '0'
    data["correct_answers"]["ans"] = answer
    data["params"]["df"] = sym.latex(diffeq)
    data["params"]["init_disp"] = initial_displacement
    data["params"]["init_vel"] = initial_velocity
    
    return data
