from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class SquarePyramidScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        height = self.ids.height_value.text
        if side != '' and height != '':
            side = float(side)
            height = float(height)

            volume = (side * side) * (height / 3)
            tsa = (side * side) + (2 * side) * (((side * side) / 4) + (height * height)) ** (1 / 2)
            lsa = side * ((side * side) + 4 * (height * height)) ** (1 / 2)
            ar_base = side * side
            ar_face = (side / 2) * (((side * side) / 4) + (height * height)) ** (1 / 2)

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.lsa_value.text = str(round(lsa, 4))
            self.ids.ar_base_value.text = str(round(ar_base, 4))
            self.ids.ar_face_value.text = str(round(ar_face, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.lsa_value.text = ''
            self.ids.ar_base.text = ''
            self.ids.ar_face.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
