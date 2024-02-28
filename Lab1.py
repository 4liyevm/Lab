import math
e=0.001
x=float(input('x='))
s=0
a=x
b=3
c=1
while math.fabs(c)>e:
    s=s+c
    f=math.factorial(b)
    a=a*x
    c=a/f
    b=b+2
print('S=',s)