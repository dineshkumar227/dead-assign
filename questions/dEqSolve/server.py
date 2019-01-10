import sympy as sym
from random import randint
import prairielearn as pl

def generate(data):
    x = sym.symbols('x')
    f = sym.Function('f')
    A = sym.symbols('A')
    C1 = sym.symbols('C1')
    diffeq = sym.Eq(f(x).diff(x) - randint(1, 9)*f(x), randint(1,9)*x)
    ans = sym.simplify(sym.dsolve(diffeq, f(x)).rhs)
    ans = ans.subs(C1, A)

    data["params"]["a"] = sym.latex(diffeq)
    data["correct_answers"]["ans"] = pl.to_json(ans)
    data["params"]["x"] = sym.latex(x)
    data["params"]["A"] = sym.latex(A)
    return data
