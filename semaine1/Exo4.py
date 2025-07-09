u = 1.0      # float
uold = 10.   # also float

for iteration in range(2000):
    if not abs(u - uold) > 1.e-8:
        print('Convergence')
        break
    uold = u
    u = 2 * u
else:
    print('No convergence')
