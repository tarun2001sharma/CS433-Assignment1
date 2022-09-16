import re

def encrypt_substitute(s):
    lst = s.split()
    var = ''
    for i in lst:
        var += re.sub(r'[^a-zA-Z0-9]', '', i) + ' '

    var2 = ''
    lst2 = var.split()
    for i in lst2:
        var2 += ''.join(chr(ord(char) + 2) for char in i) + ' '
    return var2

def encrypt_transpose(s):
    lst = s.split()
    var = ''
    for i in lst:
        i = i[::-1]
        var += i + ' '
    return var

def decrypt_substitute(s):
    lst = s.split()
    var = ''
    for i in lst:
        var += re.sub(r'[^a-zA-Z0-9]', '', i) + ' '

    var2 = ''
    lst2 = var.split()
    for i in lst2:
        var2 += ''.join(chr(ord(char) - 2) for char in i) + ' '
    return var2

def decrypt_transpose(s):
    lst = s.split()
    var = ''
    for i in lst:
        i = i[::-1]
        var += i + ' '
    return var

def encrypt(data, crypt_no):
    if(crypt_no == '1'):
        data = data
    
    elif(crypt_no == '2'):
        data = encrypt_transpose(data)

    elif(crypt_no == '3'):
        data = encrypt_substitute(data)
    
    return data

def decrypt(data, crypt_no):
    if(crypt_no == '1'):
        data = data
    
    elif(crypt_no == '2'):
        data = decrypt_transpose(data)

    elif(crypt_no == '3'):
        data = decrypt_substitute(data)
    
    return data

