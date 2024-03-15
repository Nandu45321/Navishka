from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class QuadrilateralScreenView(Screen):
    def queans(self):
        diagonal_input = self.ids.diagonal_value.text
        perpendicular_height_1_input = self.ids.perpendicular_height_1_value.text
        perpendicular_height_2_input = self.ids.perpendicular_height_2_value.text
        if diagonal_input != '' and perpendicular_height_1_input != '' and perpendicular_height_2_input != '':
            self.ids.area_value.text = str("{:.3f}".format((1 / 2 * float(diagonal_input) * (
                    float(perpendicular_height_1_input) + float(perpendicular_height_2_input)))))
        else:
            self.ids.area_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
