import flet as ft 
#グラフの表示ページ
class graph_page:
    
    def graph(graph_data):
        save_button = ft.Ref[ft.ElevatedButton]()
        ft.AppBar(title=ft.Text("Graph"), bgcolor=ft.colors.BLUE)
        ft.Column([
            ft.Row([

            ]),
            ft.Row([
                ft.ElevatedButton(
                    "表とグラフの保存",
                    icon = ft.icons.DOWNLOAD,
                    on_click = data_save()

                )
            ])
    ])
        def data_save():
            print("saveするための処理")