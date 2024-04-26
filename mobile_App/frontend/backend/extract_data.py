import pandas as pd

def judge(file_name):
        
    file_extension = file_name.split(".")[-1]
    if file_extension== 'xlsx':
        raw_data= pd.read_excel(file_name).head()
        raw_data.dropna()
                    
    elif file_extension== 'csv':
        raw_data= pd.read_csv(file_name).head()
        raw_data.dropna()
    return raw_data