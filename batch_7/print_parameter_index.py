# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# Ask user to input string
string = input("Enter the string: ")

# Ask user to input parameter to find
parameter = input("Enter the substring to find: ")

# Check first location of parameter in string
found = False

for i in range(len(string) - len(parameter) + 1):
    if string[i:i + len(parameter)] == parameter:
        # Print index of the parameter
        print(f"Parameter index: {i}")
        found = True
        break

# Print "Parameter not found in string" if parameter is not in input string
if not found:
    print("Parameter not found in string")