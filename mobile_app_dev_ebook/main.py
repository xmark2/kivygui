import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
kivy.require("1.0.6")


class LabelTestingApp(App):
    def build(self):
        return Button(text="I can Display information over screen")


if __name__ == '__main__':
    LabelTestingApp().run()
