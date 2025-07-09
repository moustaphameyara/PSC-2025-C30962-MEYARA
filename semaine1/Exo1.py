def f(x):
    return x**2 - 0.25*x + 5

# Test value
x = -0.25

# Check if it's a zero
if f(x) == 0:
    print(f"{x} is a zero of the function.")
else:
    print(f"{x} is NOT a zero of the function. f({x}) = {f(x)}")
