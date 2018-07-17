class shape:
    
    def set_edge(self,trix):
        self.edge = int(trix)
    
    def dispaly(self):
        for i in range (1,self.edge+1):
            for j in range (1,i):
                print("*",end='')
            print('')


x=shape()
x.set_edge(8)
x.dispaly()
