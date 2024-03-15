from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class RegularPentagonScreenView(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        if side_input != '':
            self.ids.area_value.text = str(
                "{:.3f}".format((1 / 4) * ((5 * (5 + 2 * (5 ** (1 / 2)))) ** (1 / 2)) * (float(side_input) ** 2)))
            self.ids.perimeter_value.text = str("{:.3f}".format(5 * float(side_input)))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
