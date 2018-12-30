import sympy as sym

x = sym.Symbol('x')
f = sym.Function('f')

nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth"
    # add more if needed
}

#looks through tuple returned by classify_ode for instances of "linear"
def linear_check(dffEq):
    diffEq_class = sym.classify_ode(diffEq, f(x))
    if any("linear" in str_ for str_ in diffEq_class):
        return "linear"
    return "non-linear"


#TODO: Automate this instead of having a hardcoded list or use a pre-made list
dEq_list = [sym.Eq(f(x).diff(x), f(x)**2 - x**2), 
            sym.Eq(f(x).diff(x,x), f(x) + sym.exp(x)),
            sym.Eq(f(x).diff(x,4), f(x).diff(x,x) + f(x)),
            sym.Eq(f(x) * f(x).diff(x,x) - 2*f(x).diff(x), sym.tan(x)),
            sym.Eq(x**2 * f(x).diff(x,4) + 2*f(x)**3 * f(x).diff(x,x) - sym.exp(x)*f(x), 17)]

for diffEq in dEq_list:
    print(linear_check(diffEq))
    print(nth[sym.ode_order(diffEq, f(x))] + " order")
