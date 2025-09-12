#2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = [ "priyesh", "sunny", "ram", "soam", "sam", "yash"]
for name in l:
    if name.startswith("s") or name.startswith("S"):
        print("Hello " + name)
    else:
        print(name)