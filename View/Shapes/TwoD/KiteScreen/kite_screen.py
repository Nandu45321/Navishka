from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class KiteScreenView(Screen):
    def queans(self):
        diagonal_1 = self.ids.diagonal_1_value.text
        diagonal_2 = self.ids.diagonal_2_value.text
        side_1 = self.ids.side_1_value.text
        side_2 = self.ids.side_2_value.text
        if diagonal_1 != '' and diagonal_2 != '' and side_1 != '' and side_2 != '':
            self.ids.area_value.text = str(
                "{:.3f}".format((float(diagonal_1) * float(diagonal_2)) / 2))
            self.ids.perimeter_value.text = str("{:.3f}".format(2 * (float(side_1) + float(side_2))))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
