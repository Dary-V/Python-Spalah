﻿print('Hello')
print('')


def capitalize(a):
    a = str(a)
    check = ord(a[0])
    if 65 <= check <= 90:
        print(chr(check), end='')
    elif 97 <= check <= 122:
        check -= 32
        print(chr(check), end='')
    i = 1
    while i < len(a):
        checkall = ord(a[i])
        if 97 <= checkall <= 122:
            pass
        elif 65 <= checkall <= 90:
            checkall += 32
        result = chr(checkall)
        print(result, end='')
        i += 1
    return ''

f = capitalize('i Like chOkolatE!')
print(f)

print('')


def center(a, b, c=' '):
    a = str(a)
    b = int(b)
    if 0 < b < 60 and b % 2 == 0:
        half = int(b / 2)
        space = c * half
        result = space + a + space
        return result

d = center('Never give up!', 10, '-*-')
print(d)

print('')


def ljust(a, b, c=' '):
    a = str(a)
    b = int(b)
    if 0 < b < 60:
        space = c * b
        result = a + space
        return result

s = ljust('Have a great day!', 3, ' >>-->')
print(s)

print('')


def rjust(a, b, c=' '):
    a = str(a)
    b = int(b)
    if 0 < b < 60:
        space = c * b
        result = space + a
        return result

j = rjust('Start changing yourself!', 3, '. ^ . * ')
print(j)

print('')


def count(a, b):
    b = b[:] # ohhh! can't understand what I should do to make 'b' show more than 1 element!!
    a = str(a)
    t = 0
    i = 0
    while i < len(a):
        if a[i] == b:
            t += 1
        i += 1
    return t

z = count('Remember that you are just an wanderer in this world...', 'a')
print(z)

print('')
