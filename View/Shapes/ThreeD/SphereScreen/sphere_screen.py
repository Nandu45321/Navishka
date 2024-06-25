from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.metrics import dp
import math


class SphereScreenView(Screen):

    def queans(self):
        radius = self.ids.radius_value.text
        if radius != '':
            radius = float(radius)
            volume = (4 / 3) * math.pi * (radius ** 3)
            tsa = 4 * math.pi * (radius ** 2)
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
