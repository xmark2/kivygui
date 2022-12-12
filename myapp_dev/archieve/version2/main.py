from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from os import listdir
kv_path = "./kv_files/"

for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)


class main_kv(GridLayout):
    pass


class MainApp(App):
    def build(self):
        self.x = 150
        self.y = 400
        return main_kv()



if __name__ == '__main__':
    MainApp().run()
