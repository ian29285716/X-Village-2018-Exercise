from lib.stack import Stack


def dec_to_bin(dec):
    s = Stack()
    n=dec
    if n==0:
        s.push(n%2)
        n=n//2

    while n>0:
        s.push(n%2)
        n=n//2
    number=s.size()
    binary=''
    for i in range(number):
        binary=binary+str(s.pop())
    return binary

dec_to_bin(1024)  
print(dec_to_bin(1024)) 
dec_to_bin(0)  
print(dec_to_bin(0)) 
 # 回傳 101010
 # 回傳 1100100