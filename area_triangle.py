#area of triangle is calculated using the formula: area = 0.5 * base * height i.e. area = 0.5 * b * h

b = float (input("Please enter the Triangle Base: "))
h = float(input("Please enter the Triangle Height: "))

def area_triangle(b, h):
    return 0.5 * b * h
area = area_triangle(b, h)
print(f"The area of the triangle with base {b} and height {h} is: {area}")
