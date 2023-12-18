#13. Write a Python program to find if a given string starts with a given character using
#Lambda.
#Sample input: input_string = "Hello, World!", given_char = "H"
#Sample Output: True

is_start_with_char = lambda input_string, given_char: input_string[0] == given_char


input_string = "Hello, World!"
given_char = "H"

result = is_start_with_char(input_string, given_char)

print(f"String '{input_string}' starts with '{given_char}': {result}")