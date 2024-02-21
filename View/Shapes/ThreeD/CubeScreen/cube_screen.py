from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar
import math


class CubeScreenView(Screen):

    def queans(self):
        side_input = self.ids.side_value.text
        if side_input != '':
            side_input = float(side_input)
            self.ids.volume_value.hint_text = str(round(side_input ** 3, 4))
            self.ids.tsa_value.hint_text = str(round(6 * side_input ** 2, 4))
            self.ids.lsa_value.hint_text = str(round(4 * side_input ** 2, 4))
            self.ids.diagonal_value.hint_text = str(round(math.sqrt(3) * side_input, 4))
        else:
            self.ids.volume_value.hint_text = ''
            self.ids.tsa_value.hint_text = ''
            self.ids.lsa_value.hint_text = ''
            self.ids.diagonal_value.hint_text = ''
            Snackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
