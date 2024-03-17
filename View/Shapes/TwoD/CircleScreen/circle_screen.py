from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class CircleScreenView(Screen):
    def queans(self):
        radius = self.ids.radius_value.text
        if radius != '':
            self.ids.area_value.text = str("{:.3f}".format(3.141592653589793238 * (float(radius) ** 2)))
            self.ids.circumference_value.text = str(
                "{:.3f}".format(3.141592653589793238 * 2 * float(radius)))
        else:
            self.ids.area_value.text = ''
            self.ids.circumference_value.text = ''
            MDSnackbar(text="[color=#ff6961]Please fill all the required blanks[/color]", ).open()
