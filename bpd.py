import pandas as pd

df=pd.read_csv('C:\\Users\\Mukesh\\Desktop\\alt\\BPD_Arrests.csv',low_memory=False)     # Read the Sample data provided (csv format)


df=df.groupby('Age').count()    # Grouping AGE along with counting the data of each column

df.sort_values('Arrest')       # Sorting each Data in Column

maxx=max(df['Arrest'])          # Deriving the Maximum and Minimum data from the Table
minn=min(df['Arrest'])

df.reset_index(inplace=True)      # Reseting the index without Losing the Existing Index Column

dp=df.set_index("Arrest")           # Setting the index as Arrest to identify the record easily

print(dp.loc[maxx]['Age'])          # Getting the Age corresponding to maximum and minimum data in the column
print(dp.loc[minn]['Age'])
