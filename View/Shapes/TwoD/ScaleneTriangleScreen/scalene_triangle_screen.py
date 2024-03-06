from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class ScaleneTriangleScreenView(Screen):
    def queans(self):
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        side_3_input = self.ids.side_3_value.text
        if side_1_input != '' and side_2_input != '' and side_3_input != '':
            semi_perimeter = (float(side_1_input) + float(side_2_input) + float(side_3_input)) / 2
            self.ids.area_value.hint_text = str("{:.3f}".format((semi_perimeter * (
                        semi_perimeter - float(side_1_input)) * (semi_perimeter - float(side_2_input)) * (
                                                                             semi_perimeter - float(side_3_input))) ** (
                                                                            1 / 2)))
            self.ids.perimeter_value.hint_text = str("{:.3f}".format(semi_perimeter * 2))
        else:
            self.ids.area_value.hint_text = ''
            self.ids.perimeter_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
