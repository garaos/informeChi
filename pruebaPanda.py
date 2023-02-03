import pandas as pd
xls = pd.ExcelFile('datos.xlsx')
print(xls.sheet_names)
df= xls.parse('Hoja1')
print(df)