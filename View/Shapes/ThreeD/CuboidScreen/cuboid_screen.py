import math

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class CuboidScreenView(Screen):

    def queans(self):
        length = self.ids.length_value.text
        breadth = self.ids.breadth_value.text
        height = self.ids.height_value.text
        if length != '' and breadth != '' and height != '':
            length = float(length)
            breadth = float(breadth)
            height = float(height)
            self.ids.volume_value.text = str(round(length * breadth * height, 4))
            self.ids.tsa_value.text = str(round(
                2 * ((length * breadth) + (breadth * height) + (length * height)),
                4))
            self.ids.diagonal_value.text = str(
                round(math.sqrt((length ** 2) + (breadth ** 2) + (height ** 2)), 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.diagonal_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()