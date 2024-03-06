from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class RhombusScreenView(Screen):
    def queans(self):
        diagonal_1_input = self.ids.diagonal_1_value.text
        diagonal_2_input = self.ids.diagonal_2_value.text
        if diagonal_1_input != '' and diagonal_2_input != '':
            self.ids.area_value.hint_text = str(
                "{:.3f}".format((float(diagonal_1_input) * float(diagonal_2_input)) / 2))
            self.ids.perimeter_value.hint_text = str(
                "{:.3f}".format(2 * ((float(diagonal_1_input) ** 2) + (float(diagonal_2_input) ** 2)) ** (1 / 2)))
            self.ids.side_value.hint_text = str("{:.3f}".format(
                (((float(diagonal_1_input) / 2) ** 2) + ((float(diagonal_2_input) / 2) ** 2)) ** (1 / 2)))
        else:
            self.ids.area_value.hint_text = ''
            self.ids.perimeter_value.hint_text = ''
            self.ids.side_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
