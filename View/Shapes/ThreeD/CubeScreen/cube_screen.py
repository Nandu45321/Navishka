import math

from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class CubeScreenView(Screen):

    def queans(self):
        side_input = self.ids.side_value.text
        if side_input != '':
            side_input = float(side_input)
            self.ids.volume_value.text = str(round(side_input ** 3, 4))
            self.ids.tsa_value.text = str(round(6 * side_input ** 2, 4))
            self.ids.lsa_value.text = str(round(4 * side_input ** 2, 4))
            self.ids.diagonal_value.text = str(round(math.sqrt(3) * side_input, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.lsa_value.text = ''
            self.ids.diagonal_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
