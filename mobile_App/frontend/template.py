from kivy.app import App
from kivy.uix.button import Button

# アプリケーションクラスの定義
class MyApp(App):
    def build(self):
        # GUIの構築
        return Button(text='Hello, Kivy!')

# アプリケーションの起動
if __name__ == '__main__':
    MyApp().run()