# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# Ask user to input string
string = input("Input string: ")

# Ask user to input parameter to count
parameter = input("Input parameter to count: ")

# Initialize count and start index
parameter_count = 0
index = 0

# Count how many times parameter appeared in the string
while index <= len(string) - len(parameter):
    if string[index:index + len(parameter)] == parameter:
        parameter_count += 1
    index += 1

# Print count of the parameter
print(f"Count of parameter in string: {parameter_count}")