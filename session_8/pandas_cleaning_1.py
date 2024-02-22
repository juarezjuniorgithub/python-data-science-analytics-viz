import pandas as pd
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
# ramen ratings
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})

print(df)

# remove duplicate rows based on all columns
new_df = df.drop_duplicates()
print(new_df)

# remove duplicates on specific column(s), use subset
new_df = df.drop_duplicates(subset=['brand'])
print(new_df)

# remove duplicates and keep last occurrences, use keep
new_df = df.drop_duplicates(subset=['brand', 'style'], keep='last')
print(new_df)