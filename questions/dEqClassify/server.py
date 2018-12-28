import sympy as sy

x = sy.Symbol('x')
f = sy.Function('f')

nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth"
    # etc
}

def linear_check(dffEq):
    diffEq_class = sy.classify_ode(diffEq, f(x))
    if any("linear" in str_ for str_ in diffEq_class):
        return "linear"
    return "non-linear"

dEq_list = [sy.Eq(f(x).diff(x), f(x)**2 - x**2), 
            sy.Eq(f(x).diff(x,x), f(x) + sy.exp(x)),
            sy.Eq(f(x).diff(x,x,x,x), f(x).diff(x,x) + f(x)),
            sy.Eq(f(x) * f(x).diff(x,x) - 2*f(x).diff(x), sy.tan(x))]

for diffEq in dEq_list:
    print(linear_check(diffEq))
    print(nth[sy.ode_order(diffEq, f(x))] + " order")
