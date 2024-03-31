import flet as ft 
import design_main,design_logic
def main(page:ft.Page):
    page.appbar = ft.AppBar(
            title=ft.Text("MainMenu",color=ft.colors.WHITE),
            center_title=True,
            bgcolor=ft.colors.BLUE
        )
    page.bgcolor = ft.colors.WHITE
    page.views.append(ft.View("/HOME",
        [
            design_main.Homedesign(page)
        ],
        )
    )
ft.app(target= main, view = ft.AppView.WEB_BROWSER, port=65210)


