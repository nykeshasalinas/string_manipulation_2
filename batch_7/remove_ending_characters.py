# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# Ask user to input string with space characters at the end
string = input("Input string with multiple spaces at the end: ")

# Print without the space characters at the end
while string.endswith(" "):
    string = string[:-1]

print(f"'{string}'")