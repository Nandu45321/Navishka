from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class CircleScreenView(Screen):
    def queans(self):
        radius_input = self.ids.radius_value.text
        if radius_input != '':
            self.ids.area_value.text = str("{:.3f}".format(3.141592653589793238 * (float(radius_input) ** 2)))
            self.ids.circumference_value.text = str(
                "{:.3f}".format(3.141592653589793238 * 2 * float(radius_input)))
        else:
            self.ids.area_value.text = ''
            self.ids.circumference_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
