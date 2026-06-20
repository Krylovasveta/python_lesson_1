import math

def square (x):
    return x * x

n = float(input ("Введите сторону квадрата: "))

if  n.is_integer() :
    s = int (n)
else :
    s = math.ceil(n)

s = square (s)
print (s)