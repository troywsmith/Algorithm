memoize = {0:0, 1:1}
def fib(n):
  if n not in memoize.keys():
    memoize[n] = fib(n-1) + fib(n-2)
  return memoize[n]

print(fib(10))