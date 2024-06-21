from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class RectangularPyramidScreenView(Screen):

    def queans(self):
        length = self.ids.length_value.text
        breadth = self.ids.breadth_value.text
        height = self.ids.height_value.text
        if length != '' and breadth != '' and height != '':
            length = float(length)
            breadth = float(breadth)
            height = float(height)

            volume = (length * breadth * height) / 3
            tsa = (length * breadth) + length * ((((breadth / 2) ** 2) + (height * height)) ** (1 / 2)) + breadth * (
                    (((length / 2) ** 2) + (height * height)) ** (1 / 2))
            lsa = length * ((((breadth / 2) ** 2) + (height * height)) ** (1 / 2)) + breadth * (
                    (((length / 2) ** 2) + (height * height)) ** (1 / 2))
            ar_base = length * breadth

            self.ids.volume_value.text = str(round(volume, 4))
            self.ids.tsa_value.text = str(round(tsa, 4))
            self.ids.lsa_value.text = str(round(lsa, 4))
            self.ids.ar_base_value.text = str(round(ar_base, 4))
        else:
            self.ids.volume_value.text = ''
            self.ids.tsa_value.text = ''
            self.ids.lsa_value.text = ''
            self.ids.ar_base_value.text = ''
            MDSnackbar(
                MDSnackbarText(
                    text="Please fill all the required blanks",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.95,
            ).open()
