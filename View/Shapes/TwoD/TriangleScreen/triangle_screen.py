from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class TriangleScreenView(Screen):
    def queans(self):
        base = self.ids.base_value.text
        height = self.ids.height_value.text
        if base != '' and height != '':
            base = float(base)
            height = float(height)

            area = (1 / 2) * base * height

            self.ids.area_value.text = str(round(area, 3))
        else:
            self.ids.area_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill the all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
