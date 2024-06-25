import math

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class CylinderScreenView(Screen):

    def queans(self):
        radius = self.ids.radius_value.text
        height = self.ids.height_value.text
        if radius != '' and height != '':
            radius = float(radius)
            height = float(height)

            volume = (22 / 7) * radius * radius * height
            tsa = (2 * (22 / 7) * radius * height) + (2 * (22 / 7) * radius * radius)
            csa = 2 * (22 / 7) * radius * height
            ar_base = (22 / 7) * radius * radius

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.csa_value.text = str(round(csa, 4))
            self.ids.ar_base_value.text = str(round(ar_base, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.csa_value.text = ''
            self.ids.ar_base_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
