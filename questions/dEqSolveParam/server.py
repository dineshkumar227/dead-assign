import sympy as sy
from random import randint
import prairielearn as pl

def generate(data):
    x = sy.symbols('x')
    f = sy.Function('f')
    diffeq = sy.Eq(f(x).diff(x,x) + f(x), sy.sec(x))
    data["params"]["a"] = sym.latex(sy.simplify(diffeq))
    data['correct_answer']["ans"] = pl.to_json(sy.simplify(sy.dsolve(diffeq, f(x), hint = 'nth_linear_constant_coeff_variation_of_parameters')))

    return data
