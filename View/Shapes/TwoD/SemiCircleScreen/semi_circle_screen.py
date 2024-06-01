from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class SemiCircleScreenView(Screen):
    def queans(self):
        radius = self.ids.radius_value.text
        if radius != '':
            radius = float(radius)
            area = (3.141592653589793238 * (radius ** 2)) / 2
            circumference = 3.141592653589793238 * radius + 2 * radius
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
