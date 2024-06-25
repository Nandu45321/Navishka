import math

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class EllipsoidScreenView(Screen):

    def queans(self):
        x = self.ids.x_value.text
        y = self.ids.y_value.text
        z = self.ids.z_value.text
        if x != '' and y != '' and z != '':
            x = float(x)
            y = float(y)
            z = float(z)

            volume = (4 / 3) * math.pi * x * y * z
            tsa = 4 * math.pi * ((((x * y) ** 1.6075) + ((x * z) ** 1.6075) + ((y * z) ** 1.6075)) / 3) ** (1 / 1.6075)

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
