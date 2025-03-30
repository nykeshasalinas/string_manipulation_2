# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# Ask user to input string
string = input("Input string: ")

# Ask user to input the suffix to be removed
suffix = input("Input suffix to be removed: ")

# Print input without the suffix
if string.endswith(suffix):
    print("String after removing prefix:", string.strip(suffix))
else:
    print(string)