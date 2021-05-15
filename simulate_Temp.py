import pandas as pd

df = pd.read_excel (r'D://card_stock.xlsx', 'gf1-ssdc-F0363')

#print(df)
print(df.iloc[6 ,2 ])
print(df.iloc[7 ,2 ])
print(df.iloc[8 ,2 ])
print(df.iloc[11: 30,0])
