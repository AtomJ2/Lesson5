import pandas as pd
from dateutil import relativedelta
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# df = pd.DataFrame(np.random.rand(10, 5))
# df['Mean'] = df[df > 0.3].mean(axis=1)
# print(df)


# df = pd.read_csv('wells_info.csv')
# df['SpudDate'] = pd.to_datetime(df['SpudDate'])
# df['CompletionDate'] = pd.to_datetime(df['CompletionDate'])
# # relativedelta как datetime.timedelta, только круче :)
# df['Month_Difference'] = \
#     (df.apply(lambda row: relativedelta.relativedelta(row['CompletionDate'], row['SpudDate']).months, axis=1))
# print(df[['SpudDate', 'CompletionDate', 'Month_Difference']])

# df = pd.read_csv('wells_info_na.csv')
# print(df, '\n\n\n')
# numeric_columns = df.select_dtypes(include=[np.number]).columns
# df_filled = df.copy()
# df_filled[numeric_columns] = df_filled[numeric_columns].fillna(df_filled[numeric_columns].median())
# df_filled = df.fillna(df.mode().iloc[0])
# print(df_filled)

df1 = pd.read_csv('cinema_sessions.csv')
df2 = pd.read_csv('titanic_with_labels.csv')
df2 = df2[df2['sex'] != '"Не указан"']
df2['sex'] = df2['sex'].replace('м', 1)
df2['sex'] = df2['sex'].replace('ж', 0)
df2['row_number'] = df2['row_number'].fillna(df2['row_number'].max())
mean_value = df2['liters_drunk'].mean()
df2['liters_drunk'] = df2['liters_drunk'].mask(df2['liters_drunk'] < 0, mean_value)
