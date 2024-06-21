from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class DodecahedronScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            side = float(side)

            volume = ((15 + 7 * (5 ** (1 / 2))) / 4) * (side * side * side)
            tsa = 3 * ((25 + 10 * (5 ** (1 / 2))) ** (1 / 2)) * side * side

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
