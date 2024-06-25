from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class RightTriangleScreenView(Screen):
    def queans(self):
        side_1 = self.ids.side_1_value.text
        side_2 = self.ids.side_2_value.text
        if side_1 != '' and side_2 != '':
            side_1 = float(side_1)
            side_2 = float(side_2)

            area = (side_1 * side_2) / 2
            hypotenuse = ((side_1 ** 2) + (side_2 ** 2)) ** (1 / 2)
            perimeter = side_1 + side_2 + float(hypotenuse)

            self.ids.area_value.text = str(round(area, 3))
            self.ids.hypotenuse_value.text = str(round(hypotenuse, 3))
            self.ids.perimeter_value.text = str(round(perimeter, 3))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            self.ids.hypotenuse_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
