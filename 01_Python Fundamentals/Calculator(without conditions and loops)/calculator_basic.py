a=int(input("Enter first digit: "))
b=int(input("Enter second digit: "))

choice = input("enter the operation to do(+,-,x,/):")

Result = {"+":a+b,
          "-":a-b,
          "x":a*b,
          "/":a/b}

print("Result=",Result[choice])