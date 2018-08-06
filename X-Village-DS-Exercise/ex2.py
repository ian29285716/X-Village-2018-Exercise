from lib.queue import Queue

def hot_potato(name_list, num):
    number=len(name_list)
    peoplelist=Queue()
    
    for i in range(number):
        peoplelist.enqueue(name_list[i])
    
    while number>1:
        for i in range(num):
            front=peoplelist.dequeue()
            peoplelist.enqueue(front)
        peoplelist.dequeue()
        number-=1
        
    remaining_person=peoplelist.dequeue()
    return remaining_person

hot_potato(["Susan", "Brad", "Kent", "David"], 6)     
print(hot_potato(["Susan", "Brad", "Kent", "David"], 6))          # 回傳 "Brad"
hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)  # 回傳 "Susan"
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

sorted.__file__
