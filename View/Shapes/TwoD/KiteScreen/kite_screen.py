from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class KiteScreenView(Screen):
    def queans(self):
        diagonal_1_input = self.ids.diagonal_1_value.text
        diagonal_2_input = self.ids.diagonal_2_value.text
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        if diagonal_1_input != '' and diagonal_2_input != '' and side_1_input != '' and side_2_input != '':
            self.ids.area_value.text = str(
                "{:.3f}".format((float(diagonal_1_input) * float(diagonal_2_input)) / 2))
            self.ids.perimeter_value.text = str("{:.3f}".format(2 * (float(side_1_input) + float(side_2_input))))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
