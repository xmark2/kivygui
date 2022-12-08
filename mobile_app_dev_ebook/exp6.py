import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class HelloApp(App):
    def build(self):
        root = Widget()
        b1 = Button(text='Button-1', pos=(root.width, root.height))
        b2 = Button(text='Button-2', pos=(200, 200))
        root.add_widget(b1)
        root.add_widget(b2)
        return root

