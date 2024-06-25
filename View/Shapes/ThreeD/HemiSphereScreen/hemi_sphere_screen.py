import math

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class HemiSphereScreenView(Screen):

    def queans(self):
        radius = self.ids.radius_value.text
        if radius != '':
            radius = float(radius)

            volume = (2 / 3) * math.pi * (radius * radius * radius)
            tsa = 3 * math.pi * (radius * radius)
            csa = 2 * math.pi * radius * radius
            ar_base = math.pi * radius * radius
            circumference = 2 * radius * math.pi

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.csa_value.text = str(round(csa, 4))
            self.ids.ar_base_value.text = str(round(ar_base, 4))
            self.ids.circumference_value.text = str(round(circumference, 4))
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
