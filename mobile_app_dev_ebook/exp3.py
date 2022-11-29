from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainApplication(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        btn1 = Button(text='Hello')
        btn2 = Button(text='World')
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

# if __name__ == '__main__':
    # MainApplication