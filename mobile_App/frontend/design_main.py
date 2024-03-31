import flet as ft
def create_Home(page: ft.Page):
    page.appbar = ft.AppBar(
            title=ft.Text("MainMenu",color=ft.colors.WHITE),
            center_title=True,
            bgcolor=ft.colors.BLUE
        )
    page.add(
        ft.Column(
            [
                ft.Container(
                    content = ft.Text("Selection",size = 60,color=ft.colors.BLACK,font_family="selecetd_font"),
                    width = 300,
                    height = 90 ,
                    alignment= ft.alignment.center,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                    
                ),
                ft.Divider(),
                
                ft.Container(
                    content = ft.Text("EditData & Display Glaph",color=ft.colors.BLACK,font_family="selected_font"),
                    width = 300,
                    height = 50 ,
                    expand_loose = True,
                    alignment= ft.alignment.center,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                    border_radius= ft.border_radius.all(10),
                    border = ft.border.all(1,ft.colors.BLACK),
                    
                ),
                ft.Divider(),
                ft.Container(
                    content = ft.Text("nutural math calculate process",color=ft.colors.BLACK,font_family="selected_font"),
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