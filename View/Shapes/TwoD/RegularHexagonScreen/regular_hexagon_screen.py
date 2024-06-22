from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class RegularHexagonScreenView(Screen):

    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            side = float(side)
            area = ((3 * (3 ** (1 / 2))) / 2) * (side ** 2)
            perimeter = 6 * side
            self.ids.area_value.text = str(round(area, 3))
            self.ids.perimeter_value.text = str(round(perimeter, 3))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
