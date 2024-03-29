from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class RegularHeptagonScreenView(Screen):
    def queans(self):
        side = self.ids.side_value.text
        if side != '':
            self.ids.area_value.text = str("{:.3f}".format((7 / 4) * (float(side) ** 2) * 2.07652139657234))
            self.ids.perimeter_value.text = str("{:.3f}".format(7 * float(side)))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
