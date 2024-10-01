def gcd(num1,num2):
  divisor = min(num1,num2)
  dividend = max(num1,num2)
  while dividend%divisor != 0 :
    temp = dividend
    dividend = divisor 
    divisor = temp%divisor
  return divisor 

gcd(12,8)
