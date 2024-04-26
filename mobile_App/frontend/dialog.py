import flet as ft

def main(page: ft.Page):
    page.title = "AlertDialog examples"


    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("入力に問題が確認されました"),
        content=ft.Text("カッコの数足りていない、またはカッコの種類が異なる可能性があります。"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )


    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    )

ft.app(target=main)