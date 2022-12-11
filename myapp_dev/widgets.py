from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SpecialButton(Button):

    @staticmethod
    def press_it():
        print('special')


class ExitButton(Button):
    pass


class CustomLayout(BoxLayout):
    pass
