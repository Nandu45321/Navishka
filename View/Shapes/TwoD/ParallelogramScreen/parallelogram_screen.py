from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class ParallelogramScreenView(Screen):
    def queans(self):
        height_input = self.ids.height_value.text
        base_input = self.ids.base_value.text
        side_input = self.ids.side_value.text
        if height_input != '' and base_input != '' and side_input != '':
            self.ids.area_value.text = str("{:.3f}".format(float(base_input) * float(height_input)))
            self.ids.perimeter_value.text = str("{:.3f}".format(2 * (float(side_input) + float(base_input))))
            if side_input != '0':  # s**2 + h**2 + 2*h*s*((s**2 - h**2)**(1 / 2) / s)
                self.ids.diagonal_1.text = str("{:.3f}".format((float(side_input) ** 2 + float(
                    height_input) ** 2 + 2 * float(height_input) * float(side_input) * ((float(side_input) ** 2 - float(
                    height_input) ** 2) ** (1 / 2) / float(side_input))) ** (1 / 2)))
                self.ids.diagonal_2.text = str("{:.3f}".format((float(side_input) ** 2 + float(
                    height_input) ** 2 - 2 * float(height_input) * float(side_input) * ((float(side_input) ** 2 - float(
                    height_input) ** 2) ** (1 / 2) / float(side_input))) ** (1 / 2)))
            else:
                self.ids.perimeter_value.text = ''
                self.ids.diagonal_1.text = ''
                self.ids.diagonal_2.text = ''
                MDSnackbar(text="[color=#ff6961]Please fill the all the blanks for diagonals[/color]", ).open()
        else:
            self.ids.area_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
