import sys

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from View.screens import screens

if hasattr(sys, 'getandroidapilevel'):
    pass
else:
    Window.size = (324, 710)


class NavishkaApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = ScreenManager()
        self.set_current_screen("main screen")
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = '50'
        self.theme_cls.material_style = "M3"
        # self.theme_cls.accent_palette = 'Blue'

    def set_current_screen(self, name: str, switch: bool = True):
        if not self.root.has_screen(name):
            Builder.load_file(screens[name]["kv"])
            self.root.add_widget(
                screens[name]["view"]())  # Or you can add () for every screen in screens.py like MainScreenView()
        if switch:  # 425/2.65    478/2.65
            self.root.current = name
            if name == "main screen":
                self.root.transition.direction = "right"
            else:
                self.root.transition.direction = "left"


NavishkaApp().run()
