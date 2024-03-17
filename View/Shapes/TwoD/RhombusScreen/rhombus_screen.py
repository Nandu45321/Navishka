from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class RhombusScreenView(Screen):
    def queans(self):
        diagonal_1 = self.ids.diagonal_1_value.text
        diagonal_2 = self.ids.diagonal_2_value.text
        if diagonal_1 != '' and diagonal_2 != '':
            diagonal_1 = float(diagonal_1)
            diagonal_2 = float(diagonal_2)

            area = (diagonal_1 * diagonal_2) / 2
            perimeter = 2 * ((diagonal_1 ** 2) + (diagonal_2 ** 2)) ** (1 / 2)
            side = (((diagonal_1 / 2) ** 2) + ((diagonal_2 / 2) ** 2)) ** (1 / 2)

            self.ids.area_value.text = str(round(area, 3))
            self.ids.perimeter_value.text = str(round(perimeter, 3))
            self.ids.side_value.text = str(round(side, 3))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            self.ids.side_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
