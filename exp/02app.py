import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))

        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))

        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f"Hello {name}, you like {pizza} pizza and favorite color is {color}.")
        output_text = f"Hello {name}, you like {pizza} pizza and favorite color is {color}."
        self.add_widget(Label(text=output_text))

        output_text = ""
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()