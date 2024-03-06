from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar


class TrapeziumScreenView(Screen):
    def queans(self):  # par1, par2, height, side1, side2
        parallel_side_1_input = self.ids.parallel_side_1_value.text
        parallel_side_2_input = self.ids.parallel_side_2_value.text
        height_input = self.ids.height_value.text
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        if parallel_side_1_input != '' and parallel_side_2_input != '' and height_input != '':
            self.ids.area_value.hint_text = str("{:.3f}".format(
                (1 / 2) * (float(parallel_side_1_input) + float(parallel_side_2_input)) * float(height_input)))
            if side_1_input != '' and side_2_input != '':
                self.ids.perimeter_value.hint_text = str("{:.3f}".format(
                    float(parallel_side_1_input) + float(parallel_side_2_input) + float(side_1_input) + float(
                        side_2_input)))
            else:
                self.ids.perimeter_value.hint_text = ''
                MDSnackbar(text="[color=#ff6961]Please fill the all the blanks for perimeter[/color]", ).open()
        else:
            self.ids.area_value.hint_text = ''
            MDSnackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]", ).open()
