# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# Ask user to input string
string = input("Input string: ")

# Ask user to input parameter
parameter = input("Input parameter to check: ")

# Check if input starts with given parameter
if string[:len(parameter)] == parameter:
    # Print "String starts with parameter" if string starts with input parameter
    print("String starts with parameter")
else:
    # Print "String does not start with parameter" if string does not start with input parameter
    print("String does not start with parameter")