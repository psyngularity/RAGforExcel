import pandas as pd

# We can use the read_excel method to read data from an Excel file
dataframe = pd.read_excel(r'D:\EData\RAGwExcel\files\P6-SuperStoreUS-2015.xlsx')

# Let's check out the first 5 rows from our excel file
dataframe.head()
# We can check out the length of the dataframe
print(len(dataframe))

