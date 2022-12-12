from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from os import listdir

kv_path = "./kv_files/"

for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)


class SpecialButton(Button):

    @staticmethod
    def press_it():
        print('special')


class ExitButton(Button):
    pass


class CustomBoxLayout(BoxLayout):
    def press(self):
        name = self.ids.name_input.text
        print(name)

        self.ids.name_label.text = f"Hello {name}!"

        self.ids.name_input.text = ''

    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))


class CustomLayout(BoxLayout):
    pass


class CheckBoxLayout(BoxLayout):
    checks = []

    def checkbox_click(self, instance, value, topping):
        if value:
            CheckBoxLayout.checks.append(topping)
            self.ids.checkbox_output_label.text = f'You selected: {CheckBoxLayout.checks}'
        else:
            CheckBoxLayout.checks.remove(topping)
            self.ids.checkbox_output_label.text = f'You selected: {CheckBoxLayout.checks}'


class Tools(App):
    def build(self):
        return CustomLayout()


if __name__ == '__main__':
    Tools().run()
