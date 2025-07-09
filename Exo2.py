import cmath
import math

# Values
x = math.pi / 4  # 45 degrees
n = 3

# Left side: (cos x + i sin x)^n
z = cmath.cos(x) + 1j * cmath.sin(x)
left_side = z**n

# Right side: cos(nx) + i sin(nx)
right_side = cmath.cos(n * x) + 1j * cmath.sin(n * x)

# Output and comparison
print("Left side: ", left_side)
print("Right side:", right_side)

# Check if they are (approximately) equal
if abs(left_side - right_side) < 1e-10:
    print("De Moivre’s formula holds for x = π/4 and n = 3.")
else:
    print("The formula does NOT hold.")
