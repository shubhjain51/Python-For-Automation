import math
p= 100000
r=.08
t=2
n=2  # compounding frequency per annum
a= 1 + r/n
print(a)
b= n*t
print(b)
c= math.pow(a,b)
print(c)
CI= p*c - p

print("The Compound interest is ", CI)