from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class RhombusScreenView(Screen):
    def queans(self):
        diagonal_1 = self.ids.diagonal_1_value.text
        diagonal_2 = self.ids.diagonal_2_value.text
        if diagonal_1 != '' and diagonal_2 != '':
            self.ids.area_value.text = str(
                "{:.3f}".format((float(diagonal_1) * float(diagonal_2)) / 2))
            self.ids.perimeter_value.text = str(
                "{:.3f}".format(2 * ((float(diagonal_1) ** 2) + (float(diagonal_2) ** 2)) ** (1 / 2)))
            self.ids.side_value.text = str("{:.3f}".format(
                (((float(diagonal_1) / 2) ** 2) + ((float(diagonal_2) / 2) ** 2)) ** (1 / 2)))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            self.ids.side_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
