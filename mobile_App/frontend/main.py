from ctypes import alignment
import flet as ft
import form_module
def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text("MainMenu",color=ft.colors.WHITE),
                        center_title=True,
                        bgcolor=ft.colors.BLUE
        ),
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
                ],
                bgcolor=ft.colors.WHITE,
            )
        )
        if page.route == "/mathLogic":
            page.views.append(
                ft.View(
                    "/mathLogic",
                    [
                    ft.Column(
                        [
                        ft.Container(
                        ft.Text("ここではグラフ化する前にデータの編集と修正を行うことができる。以下のフォームにファイルをドラッグ＆ドロップしてアップロードしてください。",color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER ),
                        height = 100,
                        width=300,
                        
                        
                        ),
                        ft.Container(
                            width=400,
                            height=200,
                            alignment = ft.alignment.center,
                            
                            border_radius=10,
                            border = ft.border.all(color = ft.colors.BLACK),
                            content = ft.Text("ファイルのアップロード"),
                            
                        ),
                            ],
                            spacing=100,
                            alignment=ft.MainAxisAlignment.CENTER,
                            
                        ),
                        
                        ft.AppBar(title=ft.Text("Editting Table"), bgcolor=ft.colors.BLUE),
                        ft.Row([
                        form_module.example()],ft.MainAxisAlignment.END)
                    ],
                    bgcolor = ft.colors.WHITE
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    


ft.app(target=main, view=ft.AppView.WEB_BROWSER)



