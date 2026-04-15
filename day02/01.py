import pandas as pd

# df = pd.read_csv('data.csv')
df = pd.read_json('data.json')

# print(df.to_string())
# print(df.head(5))
# print(df.tail(10))
print(df.info())