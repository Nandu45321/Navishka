from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar


class RightTriangleScreenView(Screen):
    def queans(self):
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        if side_1_input != '' and side_2_input != '':
            self.ids.area_value.hint_text = str("{:.3f}".format((float(side_1_input) * float(side_2_input)) / 2))
            self.ids.hypotenuse_value.hint_text = str("{:.3f}".format(((float(side_1_input) ** 2) + (float(side_2_input) ** 2)) ** (1 / 2)))
            self.ids.perimeter_value.hint_text = str("{:.3f}".format(float(side_1_input) + float(side_2_input) + float(self.ids.hypotenuse_value.hint_text)))
        else:
            self.ids.area_value.hint_text = ''
            self.ids.perimeter_value.hint_text = ''
            self.ids.hypotenuse_value.hint_text = ''
            Snackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()

