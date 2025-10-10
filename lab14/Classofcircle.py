class Circle:
    def __init__(r,radius):
        r.radius=radius
    def area(r):
        return 3.14*r.radius*r.radius
    def perimeter(r):
        return 2*3.14*r.radius
c1=Circle(10)
print("Area of circle:",c1.area())
print("Perimeter of circle:",c1.perimeter())