# factorials using function calls

def fac(n):

    if n<0:
        return "not defined beacause it is negative."
    elif n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
    


n = int(input("enter any number to find its factorail : "))
result = fac(n)
print(f"the factorial of num {n} is {result}")