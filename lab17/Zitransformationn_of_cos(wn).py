import sympy as sp
#define symbols
n,z,w=sp.symbols('n z w')
#define the function x[n]=cos(wn)u[n]
x_n=sp.cos(w*n)
#z-tranformation of x_n
X_z=sp.summation(x_n*z**(-n),(n,0,sp.oo))
print("Z-transform of x[n]=cos(wn)u[n] is \n")
sp.pprint(X_z,use_unicode=True)