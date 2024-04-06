#excelファイルまたはcsvファイルのpivotの生成
import pandas as pd
raw_data= pd.read_csv()
df= pd.DataFrame(raw_data)
tateretu= df.index
yokoretu= df.columns
aggfunc= ""

def pivot(raw_data):
    exdata= raw_data.pivot_table(tateretu, yokoretu, fill_value= 0)
    return exdata

