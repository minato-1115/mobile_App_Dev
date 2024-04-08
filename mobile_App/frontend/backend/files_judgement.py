import pandas as pd


def judgement(data_global):
    for filename in data_global.values():
        file_extension = filename.split(".")[-1]
        
        if file_extension== 'xlsx':
            raw_data= pd.read_excel(filename)
            

        elif file_extension== 'csv':
            raw_data= pd.read_csv(filename)

    df= pd.DataFrame(raw_data)
    print(df.columns)

"""
df= pd.DataFrame(raw_data_excel)
tateretu= df.index
yokoretu= df.columns
aggfunc= "mean"
"""
