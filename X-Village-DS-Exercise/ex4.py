import time


some_list = [
    65, 81, 65, 19, 6, 28, 86, 40, 72, 27,
    76, 46, 22, 98, 49, 57, 52, 46, 47, 14,
    29, 15, 59, 74, 61, 47, 20, 33, 89, 99,
    65, 82, 84, 63, 93, 1, 42, 13, 54, 58,
    84, 17, 5, 18, 14, 14, 19, 42, 60, 77,
    17, 29, 2, 42, 42, 31, 47, 67, 15, 16,
    71, 56, 98, 46, 18, 20, 14, 36, 42, 23,
    87, 7, 5, 5, 52, 78, 76, 91, 92, 88, 38,
    66, 13, 18, 68, 96, 23, 51, 77, 93, 35,
    18, 9, 64, 51, 76, 76, 96, 5, 18
]

def Bubble_Sort(l):
    number=len(l)
    listin=l
    for j in range(number-1):
        for i in range(number-1):
            if listin[i]>listin[i+1]:
                temp=listin[i]
                listin[i]=listin[i+1]
                listin[i+1]=temp
    return listin

def Insert_Sort(l):
    number=len(l)
    listin=l
    for j in range(number-1):
        for i in range(j):
            if listin[i]>listin[i+1]:
                temp=listin[i]
                listin[i]=listin[i+1]
                listin[i+1]=temp
    return listin

start = time.time()
Bs=Bubble_Sort(some_list)

end = time.time()
print(end)

start = time.time()
Is=Insert_Sort(some_list)

end = time.time()
print(end)


Bs=Bubble_Sort(some_list)
print(Bs)

Is=Insert_Sort(some_list)
print(Is)