from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class RegularOctagonScreenView(Screen):
    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            self.ids.area_value.text = str("{:.3f}".format(2 * (1 + (2 ** (1 / 2))) * (float(side) ** 2)))
            self.ids.perimeter_value.text = str("{:.3f}".format(8 * float(side)))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
