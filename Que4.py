area_one_wall = float(input("Enter the surface area of one wall :"))
cost_exterior = float(input("Enter exterior painting cost per unit area :"))
cost_interior = float(input("Enter interior painting cost per unit area :"))


exterior_walls = 7
interior_walls = 8

total_exterior_area = exterior_walls * area_one_wall
total_interior_area = interior_walls * area_one_wall

cost_ext = total_exterior_area * cost_exterior
cost_int = total_interior_area * cost_interior
total_cost = cost_ext + cost_int

print(f"Exterior Painting Cost: {cost_ext}")
print(f"Interior Painting Cost: {cost_int}")
print(f"Total Painting Cost: {total_cost}")