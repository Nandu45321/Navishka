from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar


class RectangleScreenView(Screen):
    def queans(self):
        length_input = self.ids.length_value.text
        breadth_input = self.ids.breadth_value.text
        if length_input != '' and breadth_input != '':
            self.ids.area_value.hint_text = str("{:.3f}".format(float(length_input) * float(breadth_input)))
            self.ids.perimeter_value.hint_text = str("{:.3f}".format(2 * (float(length_input) + float(breadth_input))))
            self.ids.diagonal_value.hint_text = str("{:.3f}".format((float(length_input)**2 + float(breadth_input)**2)**(1/2)))
        else:
            self.ids.area_value.hint_text = ''
            self.ids.perimeter_value.hint_text = ''
            self.ids.diagonal_value.hint_text = ''
            Snackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()

