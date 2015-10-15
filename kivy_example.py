__author__ = 'James'

from kivy.app import App
from kivy.lang import Builder

METRES_IN_KILOMETRE = 1000
# Poor name for a constant, very little description for readability.
# Constants should also be all uppercase.

class ConvertMilesToKilometres(App):
    def build(self):
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('kivy_example.kv')
        print("Test")
        # Removed the extra ) in your text string.
        self.root.ids.output_label.text = "Enter amount to convert."
        return self.root

    def convert_lengths(self):
        self.root.ids.output_label.text = " " + self.root.ids.input_conversion.text

    def get_conversion(self):
        try:
            value = float(self.root.ids.input_conversion.text)
            return value
        except ValueError:
            return 0

    def calculate_conversion(self):
        value = self.get_conversion()
        result = value / METRES_IN_KILOMETRE
        self.root.ids.output_label.text = str(result)

    def apply_increment(self, change):
        value = self.get_conversion() + change
        self.root.ids.input_conversion.text = str(value)
        self.calculate_conversion()

ConvertMilesToKilometres().run()
