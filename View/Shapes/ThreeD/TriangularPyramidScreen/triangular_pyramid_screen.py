from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class TriangularPyramidScreenView(Screen):

    def queans(self):
        base_area = self.ids.base_area_value.text
        base_perimeter = self.ids.base_perimeter_value.text
        slant_height = self.ids.slant_height_value.text
        height = self.ids.height_value.text
        if base_area != '' and base_perimeter != '' and slant_height != '' and height != '':
            base_area = float(base_area)
            base_perimeter = float(base_perimeter)
            slant_height = float(slant_height)
            height = float(height)

            volume = (1 / 3) * base_area * height
            tsa = base_area + ((1 / 2) * (base_perimeter * slant_height))
            lsa = (1 / 2) * (base_perimeter * slant_height)

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.lsa_value.text = str(round(lsa, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.lsa_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
