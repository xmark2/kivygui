import os
from kivy.app import App
from widgets import CustomLayout
# from kivy.lang import Builder

# dir_kv = os.path.join(os.getcwd(), 'design')
# Builder.load_file(os.path.join(dir_kv, 'button.kv'))
# Builder.load_file(os.path.join(dir_kv, 'layout.kv'))
# Builder.load_file(os.path.join(dir_kv, 'myapp.kv'))


class MyAppApp(App):
    pass


if __name__ == '__main__':
    MyAppApp().run()
