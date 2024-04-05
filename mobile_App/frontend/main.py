from ctypes import alignment
import flet as ft
import pandas as pd
from typing import Dict
import os 


data_global = []
def main(page: ft.Page):
    prog_bars: Dict[str, ft.ProgressRing] = {}
    files = ft.Ref[ft.Column]()
    upload_button = ft.Ref[ft.ElevatedButton]()
    viewmatrix_button = ft.Ref[ft.ElevatedButton]()
    def file_picker_result(e: ft.FilePickerResultEvent):
        global data_global
        upload_button.current.disabled = True if e.files is None else False
        viewmatrix_button.current.disabled = True 
         #添付の確認
        prog_bars.clear()
        files.current.controls.clear()
        data_global.clear()

        if e.files is not None:
            data_global = {}
            for f in e.files:
                prog = ft.ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(ft.Row([prog, ft.Text(f.name)]))
                page.session.set(f.name, f.path)
                  #パス保存の初期化　
                data_global[f.name]= os.path.join(os.path.dirname(__file__), f.path)
                print(data_global)  

            print(data_global)
        page.update()  
#dataglobalをバックエンドにもっていって処理する。
        

    def upload_files(e):
        for read_path in data_global.values():
            testdata =pd.read_csv(read_path)
            print(testdata)
        print("アップロードが完了しました")
        upload_button.current.disabled = True
        viewmatrix_button.current.disabled = False

        page.update()
        
    
    def on_upload_progress(e: ft.FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

    file_picker = ft.FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    # hide dialog in a overlay
    page.overlay.append(file_picker)


    def route_change(route):
        page.views.clear()
        page.window_height = 1000
        page.window_width = 400
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
                            ft.ElevatedButton(
                                "Select files...",
                                icon=ft.icons.FOLDER_OPEN,
                                on_click=lambda _: file_picker.pick_files(allow_multiple=True,allowed_extensions=["xlsx","csv"]),
                            ),
                            ft.Row(ref=files),
                            ft.ElevatedButton(
                                "Upload",
                                ref=upload_button,
                                icon=ft.icons.UPLOAD,
                                on_click=upload_files,
                                disabled=True,
                                
                            ),
                        ],ft.MainAxisAlignment.START),
                            ft.ElevatedButton(
                                "表の抽出",
                                ref=viewmatrix_button,
                                icon=ft.icons.UPLOAD,
                                on_click=print("表の抽出"),
                                disabled=True,
                            ),
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

ft.app(target=main)

