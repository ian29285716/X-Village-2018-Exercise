import csv
with open('AQI_20180717092829.csv','r',encoding='utf-8-sig') as read_file:
    reader = csv.reader(read_file)
    headers = next(read_file)
    for index, rows in enumerate(reader):
        if index == 1:
            row = rows
            aqiv1=int(row[2])
            break
    
    for row in reader:
        aqiv2=int(row[2])

        if  aqiv2<aqiv1:
            location=row[0]
            country=row[1]
            aqiv=row[2]
            aqiv1=int(row[2])
    print(country,location,'空氣最好','AQI=',aqiv)