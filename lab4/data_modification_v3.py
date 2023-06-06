import pandas as pd
from sklearn.preprocessing import OneHotEncoder


# load data
df = pd.read_csv('datasets/data.csv')

# create new feature with one-hot-encoding
onehot_encoder = OneHotEncoder(sparse=False)
sex_ohe = onehot_encoder.fit_transform(df[['Sex']])
sex_ohe_df = pd.DataFrame(sex_ohe, columns=onehot_encoder.categories_[0])
df = pd.concat([df, sex_ohe_df], axis=1)

# save data
df.to_csv('datasets/data.csv', index=False)
