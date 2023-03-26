from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import x
from sympy import latex
f = Function('f')
r = dsolve(Derivative(f(x), x) - x * f(x)**2 -2 * f(x), f(x), ics={f(0): -5})
print(latex(r))