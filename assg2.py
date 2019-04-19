def f(n):
  for x in range(n):
    yield x**3

for x in f(6):
  print (x)

