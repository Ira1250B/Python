import math as m
x=m.pi
def f(x):
    f1=m.cos(2*x)
    f2=-2*(m.sin(2*x))
    f3=-4*(m.cos(2*x))
    return round(f1,5 ),round(f2,5),round(f3,5)
print("The values are: ",f(x))
    
