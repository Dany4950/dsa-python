a= 5
b=9

for i in range(a):
  for j in range(a-i-1):
    print(" ",end="")
  for k in range(i*2+1):
    print("*",end="")

  print()
for i in range(a):
  for j in range(i):
    print(" ",end="")

  for k in range(b):
    print("*",end="")
  b-=2

  print()

 # above is one approach
 