from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


# dictionary as a means of calling functions
operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}

def calculator():
  from art import logo
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  print("\n")
  for key in operations:
    print(key)          # to print corresponding values -> print(operations(key))
  
  
  keep_going = True
  
  while keep_going:  
    operation_symbol = input("Enter an operator: ")
    print("\n")
    num2 = float(input("What's the next number?: "))
    print("\n")
    
    ### passing the value of operations[operation_symbol]- which is 1 of the 4 functions above- to a var .....
    selected_operation = operations[operation_symbol]  
    ###...used here as a function in its own right while passing 2 arguments AND storing it inside var 'result'
    result = selected_operation (num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {round(result, 2)}")
    
    ### way 2:
    # for key in operations:
    #   if operation_symbol == key:
    #     result = operations[key] (num1, num2)
    #     print(f"{num1} {operation_symbol} {num2} = {result}")
  
  
    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to restart: ") == 'y':
      num1 = result
  
    # WAY 2: 
    # choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
  
    # if choice == 'y':
    #   num1 = result
      
    else:
      keep_going = False
      clear()
      
      # if I want 'n' to restart the calculator from scratch I'll use recursion -> the function, that calls itself and thus restarts the calculator from scratch: 
      calculator()      # there needs to be a condition for the function to call itself or it's gonna run forever
      

calculator()

    
