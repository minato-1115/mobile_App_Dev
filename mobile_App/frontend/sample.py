from typing import Dict
import os 
import flet as ft
import pandas as pd

data_global = None
def main(page: ft.Page):
    prog_bars: Dict[str, ft.ProgressRing] = {}
    files = ft.Ref[ft.Column]()
    upload_button = ft.Ref[ft.ElevatedButton]()

    def file_picker_result(e: ft.FilePickerResultEvent):
        global data_global
        upload_button.current.disabled = True if e.files is None else False
        prog_bars.clear()
        files.current.controls.clear()
     
        if e.files is not None:
            for f in e.files:
                prog = ft.ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(ft.Row([prog, ft.Text(f.name)]))
                page.session.set(f.name, f.path)
                csv_path = os.path.join(os.path.dirname(__file__), f.path)
                data = pd.read_csv(csv_path)
                data_global = data
               
        page.update()
    #アップロードが入ったあとの変化
    def upload_files(e):
        print(data_global)
        print("アップロードが完了しました")
    
    #ファイルの表示

    def on_upload_progress(e: ft.FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

    file_picker = ft.FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    # hide dialog in a overlay
    page.overlay.append(file_picker)


    page.add(
        ft.ElevatedButton(
            "Select files...",
            icon=ft.icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True,allowed_extensions=["xlsx","csv"]),
        ),
        ft.Column(ref=files),
        ft.ElevatedButton(
            "Upload",
            ref=upload_button,
            icon=ft.icons.UPLOAD,
            on_click=upload_files,
            disabled=True,
        ),
    )


ft.app(target=main)