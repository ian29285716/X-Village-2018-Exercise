'''
TODO: define a exception class
'''
class RelationException(Exception):
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return "Are you sure that "+self.p1+" and "+self.p2+" are in love with each other?"

def check (p1,p2):
    try:
        ra=relation[p1]
        rb=relation[p1]
    except KeyError:
        print("No relation found")
        raise RelationException(p1,p2)
    
    if relation[p1] != p2:
        print("No relation found")
        raise RelationException(p1,p2)


        # TODO: raise exception
        # TIPS: 這個地方會需要 raise 兩種 exception

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}


    
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1,p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)
 