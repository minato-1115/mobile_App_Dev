import flet as ft 
import pandas as pd

def make_Table(file_name):
    file_dir_sets = file_name
    file_data_sets = []
    key_sets = []
    key_len_sets = []
    data_values_length = [] 
    for i in range (len(file_dir_sets)):
        file = pd.read_csv(file_dir_sets[i])
        file = file.head()
        file_key = file.keys()
        key_len_sets.append(len(file_key))
        key_sets.append(file_key)
        file_value = file.values.tolist()
        file_data_sets.append(file_value)
        data_values_length.append(len(file_value))

    def main(page: ft.Page):
        page.bgcolor = ft.colors.WHITE
        for i in range(len(file_dir_sets)):

            key = key_sets[i]
            key_length =key_len_sets[i]
            value = file_data_sets[i]
            value_length= data_values_length[i]
            
            def items(key,key_length):
                item = []
                
                for i in range(key_length):
                    item.append(
                            ft.Container(
                                content = ft.Text(key[i] ,weight=ft.FontWeight.BOLD,color=ft.colors.BLACK),
                                width=150,
                                height=30,
                                alignment=ft.alignment.center,
                                border=ft.border.only(bottom=ft.border.BorderSide(1, "black"))
                                
                            )
                        )
                return item
            def data(value,key_length,value_length,row_number):
                rows = []
                for i in range(value_length):
                    row = []
                    for j in range(key_length):
                        row.append(
                            ft.Container(
                                content=ft.Text(value[i][j],weight=ft.FontWeight.BOLD,color=ft.colors.BLACK),
                                width=150,
                                alignment=ft.alignment.center,
                            )
                        )
                    rows.append(row)
                    
                return rows[row_number]
            def add_items(align: ft.CrossAxisAlignment,key_length):
                return ft.Column(
                    [
                        
                        ft.Container(
                            content=ft.Row(items(key,key_length), vertical_alignment=align),
                            
                        ),
                    ]
                )
            def add_data(align: ft.CrossAxisAlignment,key_length,row_number):
                return ft.Column(
                    [
                        
                        ft.Container(
                            content=ft.Row(data(value,key_length,value_length,row_number), vertical_alignment=align),
                            
                        ),
                    ]
                )

            page.add(add_items(ft.CrossAxisAlignment.CENTER,key_length))
            for row_number in range(value_length):
                page.add(add_data(ft.CrossAxisAlignment.CENTER,key_length,row_number))
        

        page.update()


