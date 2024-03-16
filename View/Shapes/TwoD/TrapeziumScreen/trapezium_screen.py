from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class TrapeziumScreenView(Screen):
    def queans(self):  # par1, par2, height, side1, side2
        parallel_side_1 = self.ids.parallel_side_1_value.text
        parallel_side_2 = self.ids.parallel_side_2_value.text
        height = self.ids.height_value.text
        side_1 = self.ids.side_1_value.text
        side_2 = self.ids.side_2_value.text

        if parallel_side_1 != '' and parallel_side_2 != '' and height != '':

            parallel_side_1 = float(parallel_side_1)
            parallel_side_2 = float(parallel_side_2)
            height = float(height)

            area = (1 / 2) * (parallel_side_1 + parallel_side_2) * height
            self.ids.area_value.text = str(round(area))

            if side_1 != '' and side_2 != '':

                side_1 = float(side_1)
                side_2 = float(side_2)

                perimeter = parallel_side_1 + parallel_side_2 + side_1 + side_2
                self.ids.perimeter_value.text = str(round(perimeter))
            else:
                self.ids.perimeter_value.text = ''
                MDSnackbar(
                    MDSnackbarText(
                        text="Please fill the 'side' blanks for perimeter",
                    ),
                    y=dp(24),
                    pos_hint={"center_x": 0.5},
                    size_hint_x=0.95,
                ).open()
        else:
            self.ids.area_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
