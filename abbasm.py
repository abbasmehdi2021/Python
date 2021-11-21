from math import sqrt

print("enter coefficient of x square")
a = int(input())
print("enter coefficient of x")
b = int(input())
print("enter the constant")
c = int(input())
z = b*b
y = 4*a*c
x = z - y
disc = sqrt(x)
alpha = (disc - b)/(2*a)
#alpha is root 1st
beta = (disc + b)/(-2*a)
print(alpha)
print(beta)

