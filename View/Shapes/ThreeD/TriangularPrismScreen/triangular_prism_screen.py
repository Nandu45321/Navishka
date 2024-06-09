from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class TriangularPrismScreenView(Screen):

    def queans(self):
        side1 = self.ids.side_1_value.text
        side2 = self.ids.side_2_value.text
        side3 = self.ids.side_3_value.text
        height = self.ids.height_value.text
        if side1 != '' and side2 != '' and side3 != '' and height != '':
            side1 = float(side1)
            side2 = float(side2)
            side3 = float(side3)
            height = float(height)
            s = ((side1 + side2 + side3) / 2)
            base_area = ((s * (s - side1) * (s - side2) * (s - side3)) ** (1 / 2))
            volume = base_area * height
            tsa = (2 * base_area) + ((side1 + side2 + side3) * height)
            lsa = (side1 + side2 + side3) * height
            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.lsa_value.text = str(round(lsa, 4))
            self.ids.base_area_value.text = str(round(base_area, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.lsa_value.text = ''
            self.ids.base_area_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
