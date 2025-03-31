# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# Ask user to input string
string = input("Input string: ")

# Ask user to input parameter to find
parameter = input("Input parameter to find: ")

# Check first location of parameter in string starting from last character
found = False

for i in range(len(string) - len(parameter), -1, -1):
    if string[i:i + len(parameter)] == parameter:
        print(f"Parameter index starting from last character: {i}")
        found = True
        break

# Print "Parameter not found in string" if parameter is not in input string