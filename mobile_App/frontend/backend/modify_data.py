import pandas as pd 
def dlt(data_list_a, selected_elements):
    df= pd.DataFrame(data_list_a)
    yokoretsu= df.columns
    for j in range(len(selected_elements)):
        for i in range(len(yokoretsu)):
            if selected_elements[j]== yokoretsu[i]:
                deleted_data= data_list_a.drop(selected_elements, axis= 1)
    return deleted_data