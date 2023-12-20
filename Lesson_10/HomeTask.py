import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

lst1 = []
lst2 = []
for i in lst:
    lst1.append(int(i == "human"))
    lst2.append(int(i == "robot"))
df = pd.DataFrame({'human' : lst1, 'robot' : lst2})
print(df)