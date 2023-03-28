f = int(input("Generate the factorial of > "))

if f > 0:
    out = 1
    for i in range(f + 1):
        if i != 0:
            out = out * i
    print("Factorial of " + str(f) + " is " + str(out))
else:
    print("Cannot generate a factorial of that number.")