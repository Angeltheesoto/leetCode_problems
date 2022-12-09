from math import isclose
def approx_equals(a, b):
    return isclose(a, b, rel_tol=0, abs_tol=1e-3)

print(approx_equals(175.9827, 82.25))        # false
print(approx_equals(-156.24037, -156.24038)) # True
print(approx_equals(123.2345, 123.234501))   # True
print(approx_equals(1456.3652, 1456.3641))   # false
print(approx_equals(-1.234, -1.233999))      # True
print(approx_equals(98.7655, 98.7654999))    # True
print(approx_equals(-7.28495, -7.28596))     # false
