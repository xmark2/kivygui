from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image
# from kivy.uix.floatlayout import FloatLayout

Window.size = (500, 700)

Builder.load_file('calc.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ''

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def remove(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-','')}"
        else:
            self.ids.calc_input.text = f"-{prior}"

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if prior[-1].isdigit() and '.' not in num_list[-1]:
            self.ids.calc_input.text = f"{prior}."

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        if prior[-1].isdigit():
            self.ids.calc_input.text = f"{prior}{sign}"

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)

            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        '''
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)

            self.ids.calc_input.text = str(answer)
        '''

    # def press(self):
    #     name = self.ids.name_input.text
    #     print(name)
    #
    #     self.ids.name_label.text = f"Hello {name}!"
    #
    #     self.ids.name_input.text = ''


class CalculatorApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()
