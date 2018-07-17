def Btriangle (n):
    if n<0:
        raise  ValueError("value can't less than 0")
    else:
        n=n
        for i in range (1,1+n):     #層數
            for l in range (1,n+1): #排版
                if n-l-i>-1:
                    print(end='  ')
            for k in range (1,i+1): #個別數字
                def tem(x):
                    if x==0:
                        return 1
                    else:
                        return x*tem(x-1)
                value=tem(i-1)/(tem(k-1)*tem(i-k))
                value1=int(value)
                print(value1,end='  ')
            print(end='\n')

try:
    Btriangle(-15)
except ValueError:
    print("value can't less than 0")