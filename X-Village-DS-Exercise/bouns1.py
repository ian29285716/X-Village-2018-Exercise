from lib.stack import Stack


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    n=dec_number
    while n>0:
        number=n%base
        if number>9:
            s.push(digits[number])
        else:
            s.push(n%base)
        n=n//base
    number=s.size()
    string=''
    for i in range(number):
        string=string+str(s.pop())

    return string

base_converter(1000, 16)  # 回傳 3E8
print(base_converter(1000, 16))
base_converter(700, 12)   # 回傳 4A4
print(base_converter(700, 12))