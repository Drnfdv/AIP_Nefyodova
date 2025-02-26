def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalpha())
    return cleaned == cleaned[::-1]

input_string = input("Введите строку: ")

if is_palindrome(input_string):
    print("YES")
else:
    print("NO")