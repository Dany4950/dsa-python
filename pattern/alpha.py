def numtoChar(num):
  return chr(num+65)

a = 5
for i in range(a):
  for j in range(a-i):
    print(numtoChar(j),end=" ")
   
  print()


#only line a and b 

def numtoChar(num):
  return chr(num+65)

a = 5
for i in range(a):
  for j in range(i+1):
    print(numtoChar(i),end=" ")
  print()


