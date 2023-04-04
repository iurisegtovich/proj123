from . import constants
R=constants.R

from ..numericals import grad

def f_p(t,v,n):
    return n*R*t/v

def f_v(t,p,n):
    return n*R*t/p

def f_t(p,v,n):
    return p*v/n/R

def f_a(t,p,n): #expansivity
    v = f_v(t,p,n)
    dv = grad.dif1(f_v,t,1e-3,(p,n))
    a= dv/v
    return a
