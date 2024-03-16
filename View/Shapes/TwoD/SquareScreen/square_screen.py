from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class SquareScreenView(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        if side_input != '':
            self.ids.area_value.text = str("{:.3f}".format(float(side_input) ** 2))
            self.ids.perimeter_value.text = str("{:.3f}".format(4 * float(side_input)))
            self.ids.diagonal_value.text = str("{:.3f}".format(float(side_input) * 2 ** (1 / 2)))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            self.ids.diagonal_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
