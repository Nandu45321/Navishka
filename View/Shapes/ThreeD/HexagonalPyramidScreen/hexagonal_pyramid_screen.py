from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class HexagonalPyramidScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        height = self.ids.height_value.text
        if side != '' and height != '':
            side = float(side)
            height = float(height)

            volume = ((3 ** (1 / 2)) / 2) * (side * side) * height
            tsa = ((3 * (3 ** (1 / 2))) / 2) * (side * side) + (3 * side) * (
                    (height * height) + ((3 * side * side) / 4)) ** (1 / 2)
            lsa = (3 * side) * ((height * height) + ((3 * side * side) / 4)) ** (1 / 2)
            ar_base = ((3 * (3 ** (1 / 2))) / 2) * (side * side)
            ar_face = (side / 2) * ((height * height) + ((3 * side * side) / 4)) ** (1 / 2)

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
