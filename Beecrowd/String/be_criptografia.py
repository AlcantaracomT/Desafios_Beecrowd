a = 'E'
ascii_code = ord(a)

if  97 >= ascii_code <= 122 or 65 >= ascii_code <= 90:
    a = chr(ascii_code + 3)
    print(a)