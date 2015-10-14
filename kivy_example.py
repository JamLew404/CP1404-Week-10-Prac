__author__ = 'James'

from kivy.app import App
from kivy.lang import Builder

# practice


class ConvertMilesToKilometres(App):
    def build(self):
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('kivy_example.kv')
        print("test)")
        self.root.ids.output_label.text = "Hello "
        return self.root

    def convert_lengths(self):
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

