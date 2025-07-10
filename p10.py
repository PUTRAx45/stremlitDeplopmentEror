
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'kategori': ['A', 'B', 'C', 'D', 'E'],
        'nilai': [20, 35, 30, 25, 40],
        'bebas' :[0,1,2,3,4 ]}
df = pd.DataFrame(data)

plt.figure(figsize=(10,6)) 
sns.barplot(x='kategori', y='nilai', data=data)
sns.barplot(x='kategori', y='nilai', data=df, palette=['red'])
plt.pie(df['nilai'],labels=df['kategori'],autopoct='%1.1f%%',startangle=140)
plt.title('Dagram PAI Nilai per kategori')
plt.axis('equal')
plt.show()

