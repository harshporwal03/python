import pandas as pd
from matplotlib import pyplot as plt

data = {'col_1':[3,2,1,0], 'col_2':['a','b','c','d']}
dt = pd.DataFrame.from_dict(data)
print(dt)

x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.bar(x, y)
plt.hist(x, y)
plt.scatter(x, y)
plt.show()
