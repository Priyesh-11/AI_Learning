# Write a program to detect double space in a string.

a = "priyesh is a good guy  but  sometimes he is  a  bad  guy"

print(a.find("  "))  # find function returns the index of the first occurrence of the substring. If not found, it returns -1.

print(a.replace("  ", " "))  # replace function replaces all occurrences of the substring with the new substring.