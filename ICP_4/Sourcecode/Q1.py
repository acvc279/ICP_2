import pandas as pd
data = pd.read_csv('train.csv')
data1 = pd.read_csv('test.csv')
combine = [data, data1]
print(data[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))
