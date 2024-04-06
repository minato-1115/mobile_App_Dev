import pandas as pd


def judgement(file_name):
    for filename in file_name.values():
        file_extension = filename.split(".")[-1]
        
        if file_extension== 'xlsx':
            raw_data= pd.read_excel(filename)
            

        elif file_extension== 'csv':
            raw_data= pd.read_csv(filename)
    
    
    return raw_data


"""
df= pd.DataFrame(raw_data_excel)
tateretu= df.index
yokoretu= df.columns
aggfunc= "mean"
"""
