import pandas as pd

df = pd.read_excel (r'D://card_stock.xlsx',None)
#print(df.keys())

Excel_sheets_name = df.keys()
#print(Excel_sheets_name)
#print(df.iloc[6 ,2 ])
#print(df.iloc[7 ,2 ])
#print(df.iloc[8 ,2 ])
new_data = {'sheet_name': ['test'],
	'ชื่อสินค้า/วัตถุดิบ': ['test'],
	'construction': ['test'],
	'description': ['test'],
    'column:13' : ['test'],
    'column:14' : ['test'],
    'column:15' : ['test'],
    'column:16' : ['test'],
    'column:17' : ['test'],
    'column:18' : ['test'],
    'column:19' : ['test'],
    'column:20' : ['test'],
    'column:21' : ['test'],
    'column:22' : ['test'],
    'column:23' : ['test'],
    'column:24' : ['test'],
    'column:25' : ['test'],
    'column:26' : ['test'],
    'column:27' : ['test'],
    'column:28' : ['test'],
    'column:29' : ['test'],
    'column:30' : ['test']}

df_marks = pd.DataFrame(new_data)
print('Processing......')
for data in df.keys() :
    if "gf" in data:
        #print(data)
        df2 = pd.read_excel (r'D://card_stock.xlsx',data)
        new_row = {'sheet_name':data , 'ชื่อสินค้า/วัตถุดิบ':df2.iloc[6 ,2 ], 'construction':df2.iloc[7 ,2 ],'description':df2.iloc[8 ,2 ],'column:13' : df2.iloc[11,0],'column:14' : df2.iloc[12,0],'column:15' : df2.iloc[13,0],'column:16' : df2.iloc[14,0],'column:17' : df2.iloc[15,0],'column:18' : df2.iloc[16,0],'column:19' : df2.iloc[17,0],'column:20' : df2.iloc[18,0],'column:21' : df2.iloc[19,0],'column:22' : df2.iloc[20,0],'column:23' : df2.iloc[21,0],'column:24' : df2.iloc[22,0],'column:25' : df2.iloc[23,0],'column:26' : df2.iloc[24,0],'column:27' : df2.iloc[25,0],'column:28' : df2.iloc[26,0],'column:29' : df2.iloc[27,0],'column:30' : df2.iloc[28,0]}
        #append row to the dataframe
        df_marks = df_marks.append(new_row, ignore_index=True)
        #print('\n\nNew row added to DataFrame\n--------------------------')
        #print(df2.iloc[6 ,2 ])
        #print(df2.iloc[7 ,2 ])
        #print(df2.iloc[8 ,2 ])
        #print("-------------------")


#print(df_marks)
df_marks.to_excel(r'D://card_stock_update_WithExp.xlsx', index = False)
print("Export to Excel Done")
