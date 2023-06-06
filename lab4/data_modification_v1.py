import pandas as pd


# load initial dataset
df = pd.read_csv('datasets/data.csv')

# leave only needed columns
df = df[['Pclass', 'Sex', 'Age']]

#save modified dataset
df.to_csv('datasets/data.csv', index=False)
