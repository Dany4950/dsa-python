def AllDivisors(num):
  real = num
  strr = str(num)
  lenght_strr = len(strr)
  l=[]
  for i in range(1,lenght_strr):
    while i>0:
       if real%i ==0 :
          l.append(i)
          i+=1
  return l 

AllDivisors(12)
