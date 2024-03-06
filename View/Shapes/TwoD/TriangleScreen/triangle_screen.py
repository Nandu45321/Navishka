from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class TriangleScreenView(Screen):
    def queans(self):
        base_input = self.ids.base_value.text
        height_input = self.ids.height_value.text
        if base_input != '' and height_input != '':
            self.ids.area_value.hint_text = str("{:.3f}".format((1 / 2) * float(base_input) * float(height_input)))
        else:
            self.ids.area_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
