n = int(input("Enter a number to get Pattern : "))

for i in range (n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1),end="")
    print("")