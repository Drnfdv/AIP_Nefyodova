def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True
ip_address = input("Введите IP-адрес: ")
if is_valid_ip(ip_address):
    print("YES")
else:
    print("NO")