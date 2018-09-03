import pandas as pd

df1 = pd.DataFrame(
    {
        'Property_id': [1, 2, 3,],
        'Property_name': ['property 1', 'property 2', 'property 3',],
        'NOI': [1000, 2000, 3000,],
        'Period_Year':[2018, 2018, 2018,],
        'Period_Month': [2, 2, 3,],
    }
)

print(df1)

df1.set_index(keys='Property_id', inplace=True)

print(df1)

df2 = pd.DataFrame(
    {
        'Property_id': [1, 2, 3,],
        'Revenue': [999, 888, 7777,],
        'Period_Year':[2018, 2018, 2018,],
        'Period_Month': [2, 2, 4,],
    }
)

df2.set_index(keys='Property_id', inplace=True)

df3 = df1.merge(
    right=df2,
    how='outer',
    on=['Property_id', 'Period_Year', 'Period_Month',]
)

print(df3)