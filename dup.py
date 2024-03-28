import pandas as pd


df1 = pd.read_csv(r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv')
df2 = pd.read_csv(r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv')


duplicates_df1 = df1[df1.duplicated(keep=False)]
duplicates_df2 = df2[df2.duplicated(keep=False)]


common_duplicates = pd.merge(duplicates_df1, duplicates_df2, how='inner')


print("Common Duplicate Values:")
print(common_duplicates)

