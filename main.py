import random
n = int(input("Enter the value of n: "))
print("The output is as follows: \n")
for i in range(1,n+1):
    output = " "
    if i % 3 == 0 and i % 5 == 0:
        output += "FizzBuzz"
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    else:
        output += str(i)
    print(output)
