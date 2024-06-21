import math

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class TorusScreenView(Screen):

    def queans(self):
        major_radius = self.ids.major_radius_value.text
        minor_radius = self.ids.minor_radius_value.text
        if major_radius != '' and minor_radius != '':
            major_radius = float(major_radius)
            minor_radius = float(minor_radius)

            volume = (math.pi * minor_radius * minor_radius) * (2 * math.pi * major_radius)
            tsa = (2 * math.pi * major_radius) * (2 * math.pi * minor_radius)

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''

            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
