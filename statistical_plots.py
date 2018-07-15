import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline


data =  sns.load_dataset('tips')
print(data.head())

sns.lmplot(x='total_bill',
           y='tip',
           data=data,
           hue='sex',
           palette='Set1',
           legend=True)
plt.show()
