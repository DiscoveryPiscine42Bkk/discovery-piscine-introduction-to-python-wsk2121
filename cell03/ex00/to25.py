#!/urs/bin/python3
try:
    num = int(input("Enter a number less than 25: "))
except ValueError:
    print("Error")
    exit()

if num > 25:
    print("Error")
else:
    while num < 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1            