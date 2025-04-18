'''
Given a list of 10 names, complete the program that outputs the name specified by the list index entered by the user. Use a try block to output the name and an except block to catch any IndexError exception as a variable. Output "Exception! " followed by the message from the exception variable. Output also the first element in the list if the invalid index is negative or the last element if the invalid index is positive.

Note: Python allows using a negative index to access a list, as long as the magnitude of the index is smaller than the size of the list.

Ex: If the input of the program is:

5
the program outputs:

Name: Jane
Ex: If the input of the program is:

12
the program outputs:

Exception! list index out of range
The closest name is: Johnny
Ex: If the input of the program is:

-2
the program outputs:

Name: Tyrese
Ex: If the input of the program is:

-15
the program outputs:

Exception! list index out of range
The closest name is: Ryley
'''

# Starter Code

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input("Enter an index representing the name from the list you'd like to see!"))

try:
    # Try to access the name at the given index
    print(f"Name: {names[index]}")
except IndexError as e:
    # If an IndexError occurs, print the exception and handle the invalid index
    print(f"Exception! {e}")
    if index < 0:
        print(f"The closest name is: {names[0]}")  # First element for negative index
    else:
        print(f"The closest name is: {names[-1]}")  # Last element for positive index