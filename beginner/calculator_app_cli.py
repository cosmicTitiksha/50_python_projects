# This project is 'A CALCULATOR APP' which accepts prompts from Command line Interface


# Functions for multiple operations
def add(num1,num2):
  output = num1 + num2
  return output

def sub(num1,num2):
  output = num1 - num2
  return output

def mul(num1,num2):
  output = num1 * num2
  return output

def div(num1,num2):
  if num2 == 0:
    return (f"Error: '0' can't be the second number.")
  output = num1/num2
  return output

def rem(num1,num2):
  if num2 == 0:
    return (f"Error: '0' can't be the second number.")
  output = num1 % num2
  return output

def exp(num1,num2):
  output = num1 ** num2
  return output

def fdiv(num1,num2):
  if num2 == 0:
    return (f"Error: '0' can't be the second number.")
  output = num1 // num2
  return output




looping = True
while looping:
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  operation = input("Enter the operation you want to Perform (+,-,*,/,%,**,//) or 'exit': ")
  
  # Conditions to call above functions
  if operation == '+':
    print(add(num1,num2))

  elif operation == '-':
    print(sub(num1,num2))

  elif operation == '*':
    print(mul(num1,num2))

  elif operation == '/':
    print(div(num1,num2))

  elif operation == '%':
    print(rem(num1,num2))

  elif operation == '**':
    print(exp(num1,num2))

  elif operation == '//':
    print(fdiv(num1,num2))
  
  elif operation == 'exit':
    print("Exiting calculator... Goodbye! 👋")
    looping = False

  else:
    print(f"Invalid operation {operation}.")