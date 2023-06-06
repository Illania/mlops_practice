import pandas as pd
from catboost.datasets import titanic


# create initial dataset
train_df, _ = titanic()
train_df.to_csv('datasets/data.csv', index=False)
