
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

area = (length * breadth) + (0.5 * 3.14 * (radius**2))
perimeter = (2 * length) + breadth + (3.14 * radius)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")