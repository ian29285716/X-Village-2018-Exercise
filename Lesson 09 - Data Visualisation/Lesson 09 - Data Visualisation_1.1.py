import pandas as pd
import numpy as np


table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])
matn_average=df['math_score'].mean()

classsum=df.groupby(by='class').sum()
classaverage=df.groupby(by='class').mean()
relaftion=df.corr()

print(matn_average) # total score
print(classsum)
print(classaverage)
print(relaftion)

# print(something) # mean score
# print(something) # correlation coefficient