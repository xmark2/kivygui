from kivy.app import App
from kivy.uix.widget import Widget


class MyCustomForm(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyCustomForm()


if __name__ == "__main__":
    MyApp().run()
