import sympy as sy
from random import randint
import prairielearn as pl

def generate(data):
    x = sy.symbols('x')
    f = sy.Function('f')

    diffeq = sy.Eq(f(x).diff(x) - randint(1, 9)*f(x), randint(1,9)*x)

    data["params"]["a"] = diffeq
    data['correct_answer']["ans"] = pl.to_json(sy.simplify(sy.dsolve(diffeq, f(x))))

    return data
