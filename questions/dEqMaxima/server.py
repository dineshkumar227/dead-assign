import sympy as sym

def generate(data):
    x = sym.Symbol('x')
    f = sym.Function('f')
    initial_displacement = 0
    initial_velocity = 2

# f"(x) + 3f'(x) + 2f(x) = 0
    diffeq = f(x).diff(x,2) + 3 * f(x).diff(x) + 2*f(x)

    data["correct_answers"]["ans"] = 0.69315 
    data["params"]["df"] = sym.latex(diffeq)
    data["params"]["init_disp"] = initial_displacement
    data["params"]["init_vel"] = initial_velocity
    
    return data
