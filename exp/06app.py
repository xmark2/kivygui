from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('mysixth.kv')


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        output_text = f"Hello {name}, you like {pizza} pizza and favorite color is {color}."
        # self.add_widget(Label(text=output_text))
        print(output_text)

        output_text = ""
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class AwesomeApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    AwesomeApp().run()