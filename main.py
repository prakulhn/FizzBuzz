n = int(input("Enter the value of n: "))
print("The output is as follows: \n")
for i in (1,n+1):
    output = " "
    if i % 3 == 0 and i % 5 == 0:
        output += "FizzBuzz"
    elif i % 3 == 0:
        output += "Fizz"
    elif i % 5 == 0:
        output += "Buzz"
    else:
        output += str(i)
    print(output)
