for i in range (10):
    print(f"this is line number {i}")
    if i == 5:
        break # breaks the loop when i is 5

print("loop is ended")

for i in range (10):
    if i == 7:
        continue # skips the rest of the code and goes to next iteration
    print(f"this is line number {i}")