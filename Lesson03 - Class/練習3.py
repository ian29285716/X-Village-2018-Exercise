class Map:
    def set_map(self,n):
        self.listl=[]
        self.x = n
        for i in range (self.x):
            listw=[]
            for j in range (self.x):
                k='*'
                listw.append(k)
            self.listl.append(listw)

    def set_pattern(self,p):
        self.p=p
        if p==1:
            f=int((self.x-1)/2)
            self.listl[f-1][f-1]=0
            self.listl[f-1][f]=0
            self.listl[f-1][f+1]=0
            self.listl[f][f+-1]=0
            self.listl[f+1][f]=0

    def display(self):
        for h in range(self.x):
            for p in range(self.x):
                print(self.listl[h][p],end=' ')
            print(end='\n')
y=Map()
y.set_map(5)
y.set_pattern(1)
y.display()

#建立 set_map method，傳入參數 n， 建立 nxn 地圖
#建立 set_pattern method， 傳入參數 p， 如果 p=1， 在 nxn 地圖中的中央設置 Glider圖案（如下列範例）
#建立 display method，展示地圖