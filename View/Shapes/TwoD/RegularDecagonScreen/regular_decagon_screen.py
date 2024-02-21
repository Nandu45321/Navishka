from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar


class RegularDecagonScreenView(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        if side_input != '':
            self.ids.area_value.hint_text = str("{:.3f}".format((5 / 2) * (float(side_input) ** 2) * (5 + 2 * (5 ** (1 / 2))) ** (1 / 2)))
            self.ids.perimeter_value.hint_text = str("{:.3f}".format(10 * float(side_input)))
        else:
            self.ids.area_value.hint_text = ''
            self.ids.perimeter_value.hint_text = ''
            Snackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()

