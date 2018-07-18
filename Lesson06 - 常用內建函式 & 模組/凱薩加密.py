def caesar_cipher(word,n):
    sp=''
    sp=word
    number=len(word)

    for i in range(number):
        tra=''
        wchr=''
        numberw=ord(word[i])
        if numberw<120:
            wchr=(numberw+3)
            tra=chr(wchr)
            print(tra,end='')
        else:
            wchr=(numberw-23)
            tra=chr(wchr)
            print(tra,end='')

caesar_cipher("xvillage", 3)