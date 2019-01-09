import sympy as sym

x = sym.Symbol('x')
f = sym.Function('f')

#looks through tuple returned by classify_ode for instances of "linear"
def linear_check(diffEq):
    diffEq_class = sym.classify_ode(diffEq, f(x))
    if any("linear" in str_ for str_ in diffEq_class):
        return "linear"
    return "non-linear"

def generate(data):
#TODO: Automate this instead of having a hardcoded list or use a pre-made list
    dEq_list = [sym.Eq(f(x).diff(x), f(x)**2 - x**2), 
                sym.Eq(f(x).diff(x,x), f(x) + sym.exp(x)),
                sym.Eq(f(x).diff(x,4), f(x).diff(x,x) + f(x)),
                sym.Eq(f(x) * f(x).diff(x,x) - 2*f(x).diff(x), sym.tan(x)),
                sym.Eq(x**2 * f(x).diff(x,4) + 2*f(x)**3 * f(x).diff(x,x) - sym.exp(x)*f(x), 17)]

    for i in range(len(dEq_list)):
        equation_name = chr(97+i)
        data["params"][equation_name] = dEq_list[i]
        data["correct_answers"][equation_name+"_l"] = linear_check(dEq_list[i])
        data["correct_answers"][equation_name+"_o"] = sym.ode_order(dEq_list[i], f(x))

    return data
