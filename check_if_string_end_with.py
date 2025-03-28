# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Ask user to input string
string = input("Input string: ")

# Ask user to input parameter
parameter = input("Input parameter to check: ")

if string[len(string) - len(parameter):] == parameter:
    # Print "String ends with parameter" if string ends with input parameter
    print("String ends with parameter")
else:
    # Print "String does not end with parameter" if string does not end with input parameter
    print("String does not end with parameter")