# 1. Write a program using functions to find greatest of three numbers.

def greatest(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

a = int(input("enter the first num : "))
b = int(input("enter the sec num : "))
c = int(input("enter the third num : "))

result = greatest(a,b,c)

print(f"the greatest num between {a}, {b}, {c} is {result}")