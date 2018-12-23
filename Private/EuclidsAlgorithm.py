
# Iterative Solution
# def EuclidsAlgorithm(a, b):
#     while b != 0: 
#         b, a = a % b, b
#     return a

# Recursive Solution
def EuclidsAlgorithm(a, b):
    if a % b == 0:
      return b

    if b > a:
      return EuclidsAlgorithm(b, a)
    
    return EuclidsAlgorithm(b, a % b)

print(EuclidsAlgorithm(80, 120))