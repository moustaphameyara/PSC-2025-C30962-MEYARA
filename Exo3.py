import cmath
import math

# Value of x
x = math.pi / 3  # 60 degrees

# Left side: e^(ix)
left_side = cmath.exp(1j * x)

# Right side: cos(x) + i*sin(x)
right_side = cmath.cos(x) + 1j * cmath.sin(x)

# Output results
print("Left side (e^(ix))      :", left_side)
print("Right side (cos x + i sin x):", right_side)

# Verify with a tolerance
if abs(left_side - right_side) < 1e-10:
    print("Euler’s formula holds for x = π/3.")
else:
    print("The formula does NOT hold.")
