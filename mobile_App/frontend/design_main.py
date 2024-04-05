import flet as ft
def Homedesign(page):

    page.add(
        ft.Column(
            [
                ft.Container(
                    content = ft.Text("Selection",size = 50,color=ft.colors.BLACK,font_family="selecetd_font"),
                    width = 300,
                    height = 90 ,
                    alignment= ft.alignment.center,
                    ink=True,
                ),
                ft.Divider(),
                ft.Container(
                ft.TextButton(
                
                    content = ft.Text("EditData & Display Glaph",color=ft.colors.BLACK,font_family="selected_font"),
                    width = 300,
                    height = 50 ,
                    expand_loose = True,
                    on_click=lambda _:  [print("Clickable with Ink clicked!"), page.go("/mathLogic")]
                    ),
                    
                ),
                
                ft.Divider(),
                ft.Container(
                ft.TextButton(
                
                    content = ft.Text("nutural math calculate proces",color=ft.colors.BLACK,font_family="selected_font"),
                    width = 300,
                    height = 50 ,
                    expand_loose = True,
                    on_click=lambda _:  [print("Clickable with Ink clicked!"), page.go("/mathLogic")]
                    ),
                    
                ),
                ft.Divider(),
                ft.Container(
                    content = ft.Text("example",color=ft.colors.BLACK,font_family="selected_font"),
                    width = 300,
                    height = 50 ,
                    alignment= ft.alignment.center,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                    border_radius= ft.border_radius.all(10),
                    border = ft.border.all(1,ft.colors.BLACK),
                    ),
                ft.Divider(),
                ft.Container(
                    content = ft.Text("example",color=ft.colors.BLACK,font_family="selected_font"),
                    width = 300,
                    height = 50 ,
                    alignment= ft.alignment.center,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                    border_radius= ft.border_radius.all(10),
                    border = ft.border.all(1,ft.colors.BLACK),
                    ),
                ft.Divider(),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
            )