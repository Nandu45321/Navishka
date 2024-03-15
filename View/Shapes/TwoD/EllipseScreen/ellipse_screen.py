from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class EllipseScreenView(Screen):
    def queans(self):
        semi_major_axis_input = self.ids.semi_major_axis_value.text
        semi_minor_axis_input = self.ids.semi_minor_axis_value.text
        if semi_major_axis_input != '' and semi_minor_axis_input != '':
            self.ids.area_value.text = str(
                "{:.3f}".format(3.141592653589793238 * float(semi_major_axis_input) * float(semi_minor_axis_input)))
            self.ids.circumference_value.text = str("{:.3f}".format(3.141592653589793238 * (
                    3 * (float(semi_major_axis_input) + float(semi_minor_axis_input)) - (((3 * float(
                semi_major_axis_input) + float(semi_minor_axis_input)) * (float(semi_major_axis_input) + 3 * float(
                semi_minor_axis_input))) ** (1 / 2)))))
        else:
            self.ids.area_value.text = ''
            self.ids.circumference_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
