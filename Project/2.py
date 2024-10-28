def add(a, b):
  return a+b
  
def sub(a,b):
  return a-b
  
def mult(a,b):
  return a*b
  
def div(a,b):
 if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
      
def sq(a):
  return a*a
  
def exp(a,b):
  return a**b

operation = input("Choose a function: +, -, *, /, ^2, ^b: ")
a = float(input("Enter the first number: "))

if operation in ['+', '-', '*', '/']:
    b = float(input("Enter the second number: "))
    if operation == '+':
        print("Result:", add(a, b))
    elif operation == '-':
        print("Result:", sub(a, b))
    elif operation == '*':
        print("Result:", mult(a, b))
    elif operation == '/':
        print("Result:", div(a, b))
elif operation == '*a':
    print("Result:", sq(a))
elif operation == '**b':
    b = float(input("Enter the exponent: "))
    print("Result:", exp(a, b))
else:
    print("Invalid operation selected")
