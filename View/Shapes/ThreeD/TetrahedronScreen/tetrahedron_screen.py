from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class TetrahedronScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            side = float(side)

            volume = (side * side * side) / (6 * (2 ** (1 / 2)))
            tsa = (3 ** (1 / 2)) * side * side
            ar_face = ((3 ** (1 / 2)) / 4) * side * side
            height = ((2 / 3) ** (1 / 2)) * side

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.ar_face_value.text = str(round(ar_face, 4))
            self.ids.height_value.text = str(round(height, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.ar_face_value.text = ''
            self.ids.height_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
