from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class EquilateralTriangleScreenView(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        if side_input != '':
            self.ids.area_value.hint_text = str(
                "{:.3f}".format(((3 ** (1 / 2)) / 4) * float(side_input) * float(side_input)))
            self.ids.perimeter_value.hint_text = str("{:.3f}".format(3 * float(side_input)))
        else:
            self.ids.area_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
