# Write func +-*/ 2 fractions
from fractions import Fraction

def format_fraction(f: Fraction) -> str:
    num, den = f.numerator, f.denominator
    
    # Check if it's an improper fraction (hỗn số)
    if abs(num) >= den:
        whole = num // den
        rem = abs(num) % den
        if rem == 0:
            return str(whole)
        return f"{whole},{rem}/{den}"
    else:
        return f"{num}/{den}"

# Read input
a, b = map(int, input().split())
c, d = map(int, input().split())

f1 = Fraction(a, b)
f2 = Fraction(c, d)

# Perform operations and print formatted results
print(format_fraction(f1 + f2))
print(format_fraction(f1 - f2))
print(format_fraction(f1 * f2))
print(format_fraction(f1 / f2))

