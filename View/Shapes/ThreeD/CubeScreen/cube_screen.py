import math

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class CubeScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            side = float(side)
            self.ids.volume_value.text = str(round(side ** 3, 4))
            self.ids.tsa_value.text = str(round(6 * side ** 2, 4))
            self.ids.lsa_value.text = str(round(4 * side ** 2, 4))
            self.ids.diagonal_value.text = str(round(math.sqrt(3) * side, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.lsa_value.text = ''
            self.ids.diagonal_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
