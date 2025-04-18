'''
A pedometer treats walking 2,000 steps as walking 1 mile. 

Write a steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. 

The steps_to_miles() function raises a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative.
 Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the 
 steps_to_miles() function. Use a try-except block to catch any ValueError object raised by the steps_to_miles() function and output the exception message.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input of the program is:

5345
the output of the program is:

2.67
Ex: If the input of the program is:

-3850
the output of the program is:

Exception: Negative step count entered.
'''

# Define your method here
def steps_to_miles(steps):
    # Check for negative steps and raise an exception if true
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    
    # Convert steps to miles (2000 steps = 1 mile)
    return steps / 2000

if __name__ == '__main__':
    try:
        # Prompt the user to enter step count
        steps = int(input("Enter step count: "))
        
        # Call the steps_to_miles function and print the result
        miles = steps_to_miles(steps)
        print(f'{miles:.2f}')
    
    except ValueError as e:
        # Catch and print the ValueError exception message
        print(e)