def implication(A: bool, B: bool) -> bool:
    return (not A) or B

print(implication(True, True))   # True
print(implication(True, False))  # False
print(implication(False, True))  # True
print(implication(False, False)) # True
