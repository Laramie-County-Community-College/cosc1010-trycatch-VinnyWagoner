isError = True
num1 = 11

while isError == True and num1 > 10:
  try:
    num1 = int(input("Enter a whole number less than 10"))
    isError = False

    if num1 > 10:
      print("You must enter a number less than 10")
      isError = True  
  
  except ValueError:
    print("You must enter a whole number.")
    
  
# What data type is the isError variable?
  # The isError variable is a Boolean (bool) because it stores either True or False.

# What is the purpose of the isError variable?
  # The isError variable makes sure the loop keeps running until the user enters a valid number (less than 10). If the input is invalid, it sets isError to True to prompt the user again.

# Give two example of input that would trigger the except code.  
  # "abc" — This is a non-number input, so it triggers the ValueError exception.
  #5.5" — A decimal number will cause a ValueError because the program expects a whole number.

# Give an example of input that would trigger the 'You must enter a number less than 10' error message.
  # "15" — This is greater than 10, so it triggers the message: "You must enter a number less than 10".