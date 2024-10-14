def f(x):
    return x+16
def g(x,y):
    return f(x*y) + (y**2)/6 + (3*x)
def h(x,y,z):
    return g(f(z), (x**2*y**4)**(1/2))+(x*z)/(y*2)+7*z

x = float(input())
y = float(input())
z = float(input())
print(f"{f(x):.3f}\n{g(x,y):.3f}\n{h(x,y,z):.3f}")