class Map:
    def __init__(self,n,p):
        self.listl=[]
        self.x = n
        for i in range (self.x):
            listw=[]
            for j in range (self.x):
                k='*'
                listw.append(k)
            self.listl.append(listw)

        self.p=p
        if p==1:
            self.listl[1][1]=0
            self.listl[1][2]=0
            self.listl[1][3]=0
            self.listl[2][1]=0
            self.listl[3][2]=0

    def display(self):
        for h in range(self.x):
            for p in range(self.x):
                print(self.listl[h][p],end=' ')
            print(end='\n')

y=Map(5,1)

y.display()

#建立 set_map method，傳入參數 n， 建立 nxn 地圖
#建立 set_pattern method， 傳入參數 p， 如果 p=1， 在 nxn 地圖中的中央設置 Glider圖案（如下列範例）
#建立 display method，展示地圖