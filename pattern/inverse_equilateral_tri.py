a= 5
b=9
for i in range(a):
  for j in range(i):
    print(" ",end="")

  for k in range(b):
    print("*",end="")
  b-=2

  print()
