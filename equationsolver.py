from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import x
from sympy import latex
f = Function('f')
a = dsolve(Derivative(f(x), x, x) - f(x) + x, f(x),ics={f(1):1,f(2):3})
print(latex(a))