import math

from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class CuboidScreenView(Screen):

    def queans(self):
        length_input = self.ids.length_value.text
        breadth_input = self.ids.breadth_value.text
        height_input = self.ids.height_value.text
        if length_input != '' and breadth_input != '' and height_input != '':
            length_input = float(length_input)
            breadth_input = float(breadth_input)
            height_input = float(height_input)
            self.ids.volume_value.hint_text = str(round(length_input * breadth_input * height_input, 4))
            self.ids.tsa_value.hint_text = str(round(
                2 * ((length_input * breadth_input) + (breadth_input * height_input) + (length_input * height_input)),
                4))
            self.ids.diagonal_value.hint_text = str(
                round(math.sqrt((length_input ** 2) + (breadth_input ** 2) + (height_input ** 2)), 4))
        else:
            self.ids.volume_value.hint_text = ''
            self.ids.tsa_value.hint_text = ''
            self.ids.diagonal_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
