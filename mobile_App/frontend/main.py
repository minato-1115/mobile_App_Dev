
import flet as ft
import pandas as pd
from typing import Dict
import os 
import backend.extract_data  as ex_data
import backend.modify_data as modified_data
data_global = {}
checkboxes_list = []
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
            
            for f in e.files:
                prog = ft.ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(ft.Row([prog, ft.Text(f.name)]))
                page.session.set(f.name, f.path)
                  #パス保存の初期化　
                data_global[f.name]= os.path.join(os.path.dirname(__file__), f.path)
                print(data_global)  

            print(list(data_global.values()))
        page.update()  
#dataglobalをバックエンドにもっていって処理する。
        

    def upload_files(e):
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
                        
                        ft.AppBar(title=ft.Text("Select Data"), bgcolor=ft.colors.BLUE),
                        ft.Row([
                            ft.ElevatedButton(
                                "Select files...",
                                icon=ft.icons.FOLDER_OPEN,
                                on_click=lambda _: file_picker.pick_files(allow_multiple=True,allowed_extensions=["xlsx","csv"]),
                            ),
                            ft.Row(ref=files),
                            
                        ],ft.MainAxisAlignment.START),
                        ft.Row([
                            ft.ElevatedButton(
                                "Upload",
                                ref=upload_button,
                                icon=ft.icons.UPLOAD,
                                on_click=upload_files,
                                disabled=True,
                                
                            ),
                            ]),
                            ft.ElevatedButton(
                                "表の抽出",
                                ref=viewmatrix_button,
                                icon=ft.icons.DOWNLOADING,
                                on_click=lambda _:  [print("Clickable with Ink clicked!"), page.go("/mathLogic/extractTable")],
                                disabled=True,
                            ),
                    ],
                    bgcolor = ft.colors.WHITE
                )
            )
            
        elif page.route == "/mathLogic/extractTable":
            label_key= []

            def on_change(e):
        # チェックボックスの状態が変化したときの処理
                if e.control.value:
                    print(f"{e.control.label} selected")
                    #ここでクリックしたら名前の保存
                    # 選択されたラベルに応じた処理を追加
                    print(e.control.label)
                    label_key.append(str(e.control.label))

                    
                else:
                    print(f"{e.control.label} deselected")
                    label_key.remove(str(e.control.label))
                print(label_key)
                
                    #ここでクリックしたら名前の削除
            #ここに選択された項目名から削除された表を再表示する指示を行う

            file_name = data_global.values()
            def items(key):
                item = []
                for k in key:
                    item.append(ft.Container(
                        content=ft.Text(k, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        width=150,
                        height=30,
                        alignment=ft.alignment.center,
                        border=ft.Border(bottom=ft.BorderSide(1, "black"))
                    ))
                    
                return item
            
            def check_boxes(key):
                
                checkboxes = []
        # keys配列からチェックボックスを作成
                for k in key:
                    
                    checkbox = ft.Checkbox(
                        label=k,
                        on_change=on_change  # チェックボックスの状態変化時に呼び出されるイベントハンドラ
                    )
                    checkboxes_list.append(k)
                    checkboxes.append(checkbox)

                # チェックボックスを含むColumnを作成
                checkbox_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
                for checkbox in checkboxes:
                    checkbox_row.controls.append(checkbox)

                return checkbox_row
            
            def data(value):
                rows = []
                for v in value:
                    row = [ft.Container(
                        content=ft.Text(val, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        width=150,
                        alignment=ft.alignment.center,
                    ) for val in v]
                    rows.append(row)
                return rows
            
            def make_Table():
                
                container = ft.Column()
                for file_path in file_name:
                    file = ex_data.judge(file_path)
        #ここでcheckboxにデータが格納されているときに、checkboxesのデータを利用して表を作る           
                    if label_key :
                        print("表の列を削除")
                        file = modified_data(file,label_key)
                        #岩崎君の関数追加
                    keys = list(file.keys())
                    values = file.values.tolist()

                    header_row = ft.Row(controls=items(keys), alignment=ft.MainAxisAlignment.CENTER)
                    container.controls.append(header_row)
                    

                    for value_row in data(values):
                        data_row = ft.Row(controls=value_row, alignment=ft.MainAxisAlignment.CENTER)
                        container.controls.append(data_row)
                    
                    container.controls.append(ft.Text("削除したい項目", weight=ft.FontWeight.BOLD,color=ft.colors.BLACK))
                    checkbox =  check_boxes(keys)
                    container.controls.append(checkbox)

                return container
            
            def refresh_table(e):
    # テーブルを再構築する処理
                container = make_Table()  # make_Tableはページオブジェクトを受け取るように変更
                page.controls.clear()  # 既存のコンテンツをクリア
                page.add(container)  # 新しいコンテナを追加
                page.update()

            page.views.append(
                ft.View(
                    "/mathLogic/extractTable",
                    [
                    ft.Column(
                        [
                        ft.Container(
                        ft.Text("ここでは表の抽出を行います。注意、表の列削除の際に同じキー値が複数の表で含まれる場合、削除されます。改善の余地はございますがご理解のほどよろしくお願いします。",color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER ),
                        height = 100,
                        width=300,     
                        ),
                            ],
                            spacing=100,
                            alignment=ft.MainAxisAlignment.CENTER,
                            
                        ),
                       make_Table(),
                       
                        ft.AppBar(title=ft.Text("extract table"), bgcolor=ft.colors.BLUE),
                        ft.Row([
                            ft.ElevatedButton(text="データの編集", on_click=lambda e: [refresh_table(e),print(label_key),page.update()])
                            ]),
                        ft.Row([
                            ft.ElevatedButton(
                                "グラフの表示",
                                on_click=print("アラートを出す。結果の出力前に確認してもらう"),
                            ),
                        #アラートの結果出力yesであれば次のページに移動し、出力、Noであれば、出力せずになにも起こさない
                            ]),
                            
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