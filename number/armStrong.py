def Armstrong(num):
  l =[]
  real = num
  strr = str(num)
  for i in range(len(str(num))):
    l.append(int(strr[i]))
  length = len(l)

  summ = 0 

  for i in l :
    power = i**length
    summ += power
  if summ == real:
    return True 
  return False 
  
Armstrong(153)

# output : True 