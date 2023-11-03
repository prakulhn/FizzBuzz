n = int(input("Enter the value of n: "))
a = range(1, n+1)
print("The output is as follows: ")
for i in a:
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
