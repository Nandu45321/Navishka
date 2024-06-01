from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class EllipseScreenView(Screen):
    def queans(self):
        semi_major_axis = self.ids.semi_major_axis_value.text
        semi_minor_axis = self.ids.semi_minor_axis_value.text
        if semi_major_axis != '' and semi_minor_axis != '':
            semi_major_axis = float(semi_major_axis)
            semi_minor_axis = float(semi_minor_axis)

            area = 3.141592653589793238 * semi_major_axis * semi_minor_axis
            circumference = 3.141592653589793238 * (
                    3 * (semi_major_axis + semi_minor_axis) - (((3 * semi_major_axis + semi_minor_axis) * (
                    semi_major_axis + 3 * semi_minor_axis))) ** (1 / 2))

            self.ids.area_value.text = str(round(area, 3))
            self.ids.circumference_value.text = str(round(circumference, 3))
        else:
            self.ids.area_value.text = ''
            self.ids.circumference_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()