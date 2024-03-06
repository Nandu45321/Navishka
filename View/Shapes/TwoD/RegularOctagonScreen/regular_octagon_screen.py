from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class RegularOctagonScreenView(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        if side_input != '':
            self.ids.area_value.hint_text = str("{:.3f}".format(2 * (1 + (2 ** (1 / 2))) * (float(side_input) ** 2)))
            self.ids.perimeter_value.hint_text = str("{:.3f}".format(8 * float(side_input)))
        else:
            self.ids.area_value.hint_text = ''
            self.ids.perimeter_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
