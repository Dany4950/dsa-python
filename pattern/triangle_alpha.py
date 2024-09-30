def numtochar(num):
  return chr(num+65)

a = 5 
for i in range(a-1):
  for j in range(a-i-2):
    print(" " , end="")

  for j in range(i+1)  :
    print(numtochar(j),end="")

  for j in range(i):
    print(numtochar(j),end="")
  print()

#    A
#   ABA
#  ABCAB
# ABCDABC

# above we see the pattern 