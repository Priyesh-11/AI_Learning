def sum(n):

    if n<0:
        return "not defined beacause it is negative."
    elif n==0 or n==1:
        return 1
    else:
        return n+sum(n-1)
    


n = int(input("enter any number to find its Sum : "))
result = sum(n)
print(f"the Sumtorial of num {n} is {result}")