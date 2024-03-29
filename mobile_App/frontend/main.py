import flet as ft 
def main(page:ft.Page):
    page.bgcolor = "#ffff"
    page.fonts = {
        "selecetd_font":"fonts/KiwiMaru-Medium.ttf"
    }

    page.appbar = ft.AppBar(
    title=ft.Text("MainMenu"),
    center_title=True,
    bgcolor=ft.colors.BLUE
    )

    page.add(
    ft.Container(
        content = ft.Text("Selection",size = 50,color=ft.colors.BLACK,font_family="selected_font"),
        width = 300,
        height = 50 ,
        ink=True,
        on_click=lambda e: print("Clickable with Ink clicked!"),
        
    ),
    ft.Container(
        content = ft.Text("EditData & Display Glaph",color=ft.colors.BLACK,font_family="selected_font"),
        width = 300,
        height = 50 ,
        bgcolor= ft.colors.BLUE_GREY_100,
        ink=True,
        on_click=lambda e: print("Clickable with Ink clicked!"),
        border_radius= ft.border_radius.all(10),
        border = ft.border.all(1,ft.colors.BLACK),
        
    ),
    ft.Container(
        content = ft.Text("nutural math calculate process",color=ft.colors.BLACK,font_family="selected_font"),
        width = 300,
        height = 50 ,
        bgcolor= ft.colors.BLUE_GREY_100,
        ink=True,
        on_click=lambda e: print("Clickable with Ink clicked!"),
        border_radius= ft.border_radius.all(10),
        border = ft.border.all(1,ft.colors.BLACK),
        
    ),
        )
            
ft.app(target= main, view = ft.WEB_BROWSER, port=65210)