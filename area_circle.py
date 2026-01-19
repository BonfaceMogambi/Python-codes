#Area of circle is calculated using the formula: area = π * r^2 i.e. area = 22/7 * r * r

r = float(input("Please enter the radius of the circle: "))

def area_circle(r):
    pi = 22/7
    return pi * r * r
area = area_circle(r)
print(f"The area of the circle with radius {r} is: {area}")