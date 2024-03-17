from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class RegularDecagonScreenView(Screen):
    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            self.ids.area_value.text = str(
                "{:.3f}".format((5 / 2) * (float(side) ** 2) * (5 + 2 * (5 ** (1 / 2))) ** (1 / 2)))
            self.ids.perimeter_value.text = str("{:.3f}".format(10 * float(side)))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
