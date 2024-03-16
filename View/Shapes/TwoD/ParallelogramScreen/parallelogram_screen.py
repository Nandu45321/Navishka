from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class ParallelogramScreenView(Screen):
    def queans(self):
        height = self.ids.height_value.text
        base = self.ids.base_value.text
        side = self.ids.side_value.text
        if height != '' and base != '' and side != '' and float(side) >= float(height):
            height = float(height)
            base = float(base)
            side = float(side)

            area = base * height
            perimeter = 2 * (side + base)
            diagonal_1 = (side ** 2 + height ** 2 + 2 * height * side * (
                    (side ** 2 - height ** 2) ** (1 / 2) / side)) ** (1 / 2)
            diagonal_2 = (side ** 2 + height ** 2 - 2 * height * side * (
                    (side ** 2 - height ** 2) ** (1 / 2) / side)) ** (1 / 2)

            self.ids.area_value.text = str(round(area))
            self.ids.perimeter_value.text = str(round(perimeter))
            self.ids.diagonal_1.text = str(round(diagonal_1))
            self.ids.diagonal_2.text = str(round(diagonal_2))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            self.ids.diagonal_1.text = ''
            self.ids.diagonal_2.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please enter valid inputs",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
