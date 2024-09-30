# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 

n=5
a = 10
for i in range(5):
  for j in range(n-i):
    print("*", end=" ")
  for j in range(i):
    print(" " , end=" ")
  for j in range(i):
    print(" ",end=" ")
  for j in range(n-i):
    print("*",end=" ")
  print()

for i in range(5):
  for j in range(i+1):
    print("*",end=" ")
  for j in range(5-i-1):
    print(" ",end=" ")
  for j in range(5-i-1):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
 

  print()
