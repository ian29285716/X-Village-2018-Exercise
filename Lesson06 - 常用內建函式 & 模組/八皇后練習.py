plane=[]

for i in range (8):
    listcols=[]
    for j in range (8):
        listcols.append(0)
    plane.append(listcols)


def eight_queens(n):
    eight=n
    for l in range(8):
        x=eight[l][0]
        y=eight[l][1]
        plane[x][y]=1
    for i in range (8):
        rowsum=sum(plane[i])
        if rowsum>1:            #橫向加總
                return flase
        
        colsum=0                #直向加總
        for j in range (8):
            colsum+=(plane[i][j])  
        if colsum>1:            
            return flase
        
        colsum=0                #左上斜向加總
        for k in range(i+1):
            d=i-k
            colsum+=(plane[d][k])
        if colsum>1:
            return flase
        
        colsum=0
        for h in range(i+1):       #左下斜向加總
            f=7-i
            x=f+h
            colsum+=(plane[f][h])
        if colsum>1:
            return flase
        
        colsum=0
        for n in range(i+1):       #右上斜向加總
            b=7-i
            x=b+n
            colsum+=(plane[n][x])
        print('\n')
        if colsum>1:
            return flase

        colsum=0
        for z in range(i+1):       #右下斜向加總
            q=7-z
            d=7-i+z
            colsum+=(plane[d][q])
        if colsum>1:
            return flase




        


eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])