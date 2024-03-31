import flet as ft 
import design_main
def main(page:ft.Page):
    page.appbar = ft.AppBar(
            title=ft.Text("MainMenu",color=ft.colors.WHITE),
            center_title=True,
            bgcolor=ft.colors.BLUE
        )
    page.bgcolor = ft.colors.WHITE
    page.fonts = {
        "selecetd_font":"fonts/KiwiMaru-Medium.ttf"
    }
    
    page.views.append(design_main.create_Home(page))
    """
    def main(page:ft.Page):
    page.appbar = ft.AppBar(
            title=ft.Text("MainMenu",color=ft.colors.WHITE),
            center_title=True,
            bgcolor=ft.colors.BLUE
        )
    page.bgcolor = ft.colors.WHITE
    page.fonts = {
        "selecetd_font":"fonts/KiwiMaru-Medium.ttf"
    }
    
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

    def route_chnge(handler):
        troute = ft.TemplateRoute(handler.route)
        if troute.match("/HOME"):
            page.views.append(create_Home)
        elif troute.match("/GraphicsDesign"):
            page.views.append()

    
if __name__ == "main": 
    ft.app(target= main, view = ft.WEB_BROWSER, port=65210)
    """
ft.app(target= main, view = ft.WEB_BROWSER, port=65210)