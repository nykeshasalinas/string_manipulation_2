# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# Ask user to input string
string = input("Input string: ")

# Ask user to input length of space to add at the end of string
space = int(input("Input length of space to add: "))

# Print input with desired spaces
if len(string) < space:
    string = string + " " * (space - len(string))

print("String after padding:", repr(string))