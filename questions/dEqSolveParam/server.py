import sympy as sym
from random import randint
import prairielearn as pl

def generate(data):
    x = sym.symbols('x')
    f = sym.Function('f')
    C1, C2 = sym.symbols('C1, C2')
    A = sym.symbols('A')
    B = sym.symbols('B')
    diffeq = sym.Eq(f(x).diff(x,x) + f(x), sym.sec(x))
    ans = (sym.simplify(sym.dsolve(diffeq, f(x), hint = 'nth_linear_constant_coeff_variation_of_parameters').rhs))
    ans = ans.subs([(C1, A), (C2,B)])

    data["params"]["x"] = sym.latex(x)
    data["params"]["a"] = sym.latex(sym.simplify(diffeq))
    data["correct_answers"]["ans"] = pl.to_json(ans)
    data["params"]["A"] = sym.latex(A)
    data["params"]["B"] = sym.latex(B)

    return data
