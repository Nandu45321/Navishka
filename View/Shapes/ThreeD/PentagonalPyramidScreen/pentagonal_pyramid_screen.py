import math

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class PentagonalPyramidScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        height = self.ids.height_value.text
        if side != '' and height != '':
            side = float(side)
            height = float(height)

            s = math.tan(3*math.pi/10)  # tan(3pi/10) = 1.37....
            volume = (5 / 12) * s * height * (side * side)
            tsa = (5 / 4) * s * (side * side) + (5 * (side / 2)) * ((height * height) + (((side * s) / 2) ** 2)) ** (
                        1 / 2)
            lsa = (5 * side * ((height * height) + (((side * s) / 2) ** 2)) ** (1 / 2)) / 2
            ar_base = (5 / 4) * s * side * side
            ar_face = (side / 2) * ((height * height) + (((side * s) / 2) ** 2)) ** (1 / 2)

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.lsa_value.text = str(round(lsa, 4))
            self.ids.ar_base_value.text = str(round(ar_base, 4))
            self.ids.ar_face_value.text = str(round(ar_face, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.lsa_value.text = ''
            self.ids.ar_base_value.text = ''
            self.ids.ar_face_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
