a = 4

for i in range(a):
  for j in range(i+1):
     print(j+1,end="")

  for k in range(a-i-1):
     print(" ",end="")


  for m in range(a-i-1):
    print(" ",end="")

  for n in range(i+1,0,-1): 
    print(n,end="")
  print()
  

