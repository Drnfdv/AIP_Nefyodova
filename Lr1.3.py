s = input("Введите строку: ")
result = ""

for i in range(len(s)):
    result += s[i]
    if i != len(s) - 1:
        result += "*"

print(result)