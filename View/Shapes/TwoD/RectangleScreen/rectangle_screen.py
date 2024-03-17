from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class RectangleScreenView(Screen):
    def queans(self):
        length = self.ids.length_value.text
        breadth = self.ids.breadth_value.text
        if length != '' and breadth != '':
            length = float(length)
            breadth = float(breadth)

            area = length * breadth
            perimeter = 2 * (length + breadth)
            diagonal = (length ** 2 + breadth ** 2) ** (1 / 2)

            self.ids.area_value.text = str(round(area, 3))
            self.ids.perimeter_value.text = str(round(perimeter, 3))
            self.ids.diagonal_value.text = str(round(diagonal, 3))
        else:
            self.ids.area_value.text = ''
            self.ids.perimeter_value.text = ''
            self.ids.diagonal_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
