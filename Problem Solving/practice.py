# Reverse a string without using built-in reverse functions
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("hello"))  # "olleh"