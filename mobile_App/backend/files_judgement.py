import pandas as pd

df= pd.DataFrame(raw_data_excel)
tateretu= df.index
yokoretu= df.columns
aggfunc= ""






def judgement(file_name):
    for filename in file_name.values():
    
        file_extension = filename.split(".")[-1]
        
        
        if file_extension== 'xlsx':
            raw_data_excel= pd.read_excel(filename)
            
        elif file_extension== 'csv':
            raw_data_csv= pd.read_csv(filename)

        print("File extension:", file_extension)
        return file_extension

