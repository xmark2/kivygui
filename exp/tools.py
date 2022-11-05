from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image
# from kivy.uix.floatlayout import FloatLayout

Builder.load_file('tools.kv')


class MyLayout(Widget):

    checks =[]

    def checkbox_click(self, instance, value, topping):
        if value:
            MyLayout.checks.append(topping)
            self.ids.checkbox_output_label.text = f'You selected: {MyLayout.checks}'
        else:
            MyLayout.checks.remove(topping)
            self.ids.checkbox_output_label.text = f'You selected: {MyLayout.checks}'

    def select(self, value):
        print(value)

    def switch_click(self, switchObject, switchValue):
        if switchValue:
            self.ids.switch_label.text = "Switch On"
        else:
            self.ids.switch_label.text = "Switch Off"
            # self.ids.my_switch.disabled = True

    def press_it(self):
        current = self.ids.my_progress_bar.value
        current += .25

        self.ids.my_progress_bar.value = current

    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))

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
