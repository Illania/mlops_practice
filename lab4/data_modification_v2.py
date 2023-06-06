import pandas as pd


# load initial dataset
df = pd.read_csv('datasets/data.csv')

# Fill "Age" with mean
mean_age = df['Age'].mean()

# modify datset
df['Age'].fillna(mean_age, inplace=True)

# save modified dataset
df.to_csv('datasets/data.csv', index=False)
