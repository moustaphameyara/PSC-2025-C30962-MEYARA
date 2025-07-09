def half_adder(p: int, q: int) -> tuple[int, int]:
    sum_bit = p ^ q  # XOR
    carry_bit = p & q  # AND
    return sum_bit, carry_bit

def full_adder(A: int, B: int, carry_in: int) -> tuple[int, int]:
    sum1, carry1 = half_adder(A, B)
    final_sum, carry2 = half_adder(sum1, carry_in)
    carry_out = carry1 | carry2  # OR
    return final_sum, carry_out

# Test all combinations for full adder
print("A B Cin | Sum Cout")
for A in (0, 1):
    for B in (0, 1):
        for Cin in (0, 1):
            s, c = full_adder(A, B, Cin)
            print(f"{A} {B}  {Cin}  |  {s}    {c}")
