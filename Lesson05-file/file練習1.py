f=open('note.txt','w')

date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')


f.write('輸入日期:')
f.write(date)
f.write('\n')
f.write('輸入事件:')
f.write(event)
f.write('\n')
f.write('輸入心得:')
f.write(description)
f.write('\n')

f.close()