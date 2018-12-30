import sympy as sym

x = sym.Symbol('x')
f = sym.Function('f')

diffeq = sym.Eq(f(x).diff(x,2), 3 * f(x).diff(x) - 2*f(x))
conditions = {f(0):2, f(x).diff(x).subs(x, 0): 2}

print(sym.simplify(sym.dsolve(diffeq, f(x), ics = conditions)))

