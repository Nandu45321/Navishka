from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class QuadrilateralScreenView(Screen):
    def queans(self):
        diagonal = self.ids.diagonal_value.text
        perpendicular_height_1 = self.ids.perpendicular_height_1_value.text
        perpendicular_height_2 = self.ids.perpendicular_height_2_value.text
        if diagonal != '' and perpendicular_height_1 != '' and perpendicular_height_2 != '':
            diagonal = float(diagonal)
            perpendicular_height_1 = float(perpendicular_height_1)
            perpendicular_height_2 = float(perpendicular_height_2)

            area = 1 / 2 * diagonal * (perpendicular_height_1 + perpendicular_height_2)

            self.ids.area_value.text = str(round(area, 3))
        else:
            self.ids.area_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
