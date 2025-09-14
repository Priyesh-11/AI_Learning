# 2. Write a python program using function to convert Celsius to Fahrenheit. 

def CtoF(c):
    return (c*(9/5))+32

a = float(input("enter value in celsius to get its fahrenheit : "))

print(f"the {a} in fahrenheit is {CtoF(a)}.")