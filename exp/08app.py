from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image
# from kivy.uix.floatlayout import FloatLayout

Builder.load_file('update_label.kv')


class MyLayout(Widget):
    def press(self):
        name = self.ids.name_input.text
        print(name)

        self.ids.name_label.text = f"Hello {name}!"

        self.ids.name_input.text = ''



class AwesomeApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
