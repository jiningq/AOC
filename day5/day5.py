import hashlib
import time

a = time.time()
input = 'ffykfhsq'
# part 1
def getPassword1(input):
    password = ''
    i = 0
    while len(password) < 8:
        hashtext = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hashtext.startswith('00000'):
            password += hashtext[5]
            print(i, password)
        i += 1
    return password

getPassword1('abc')
getPassword1(input)
print(time.time() - a)

b = time.time() 

# part 2
def getPassword2(input):
    password = ['_'] * 8
    i = 0
    while '_' in password:
        hashtext = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hashtext.startswith('00000'):
            if hashtext[5].isdigit():
                pos = int(hashtext[5])
                if pos < 8 and pos >= 0 and password[pos] == '_':
                    password[pos] = hashtext[6]
                    print(i, ''.join(password))
        i += 1
    return ''.join(password)

getPassword2('abc')
getPassword2(input)

print(time.time() - b)