import flet as ft
import re 

math_func = ""
def main(page: ft.Page):
     
    
    def text_edit(e):
        global math_func 
        t.value = f"{tb1.value}"
        math_func = tb1.value

        t.value = re.sub(r'\(\(([^()]+?)\)\)', r'{\1}', t.value)
        t.value = re.sub(r'\(([^()]+?)\)', r'{\1}', t.value)
        t.value = t.value.replace("*","×").replace("/","÷")
        #((のように開きカッコが連続した場合に(())→{()
        try:
            if len(t.value) >= 1:
                if t.value[1]!="=":
                    t.value = t.value[:1]+"="+t.value[1:]
        except IndexError:
            print("予期しまくりエラー")
        page.update()

#まだまだいじれるはず。あとはアラートの設定をできるようにしたい     

#    t = ft.Text(size = 30 , font_family= 'Georgia', italic = True)
    t = ft.Text("",
        style = ft.TextStyle(
                size=40,
                letter_spacing=10,
                font_family= 'Georgia',
                italic = True
                    ),
                )     
        
    field_property =r"^[A-Za-z]{1}(?:[\(\)A-Za-z0-9\s/÷\^\.]|[\+\-\*](?![\+\-\*]))*$"
    tb1 = ft.TextField(label="数式の入力をしてください。形式 y = ax+b ",on_change=text_edit, input_filter=ft.InputFilter(allow=True,regex_string = field_property, replacement_string=""))
#特殊な文字列.   ^   $   [   ]   *   +   ?   |   (   )
#演算子は連続しない
#**は使わずに^で表す　
    def close_dlg(e):
        bracket_alert.open = False
        null_alert.open = False
        page.update()

    bracket_alert = ft.AlertDialog(
        modal=True,
        content=ft.Text("カッコの数が正しくありません"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    null_alert = ft.AlertDialog(
        modal=True,
        content=ft.Text("テキストの入力を行ってください"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_modal(statement):
        if statement == "NullError" :
            page.dialog = null_alert
            null_alert.open = True
            page.update()
        elif statement == "BraError":
            page.dialog = bracket_alert
            bracket_alert.open = True
            page.update()

    def Measurement_uncertainty(e):
        open_brackets = math_func.count('(')
        close_brackets = math_func.count(')')
        if math_func == "":
            statement = "NullError"
            open_dlg_modal(statement)
        elif open_brackets != close_brackets:
            statement = "BraError"
            open_dlg_modal(statement)
            print(math_func)
        else:
            print("関数の実行")
    
    submit_button = ft.ElevatedButton("計算",on_click=Measurement_uncertainty)
    page.add(
        t,tb1,submit_button)
    
ft.app(target=main)


    
"""

import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
    tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
    tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
    tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)

ft.app(target=main)
"""