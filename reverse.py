def reverse_string(value):
    # Reverse the string using slicing
    reversed_value = value[::-1]
    return reversed_value

# Test the function
user_input = input("Enter a string to reverse: ")
reversed_input = reverse_string(user_input)
print("Reversed string:", reversed_input)
