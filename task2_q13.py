from functools import reduce

a=[1,2,3,4,5,6,7]
y=reduce(lambda a,d: 10*a+d, a, 0)
print(y)