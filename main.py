"""
    <Navishka>
    Copyright (C) <2024 and continuing>  <Yamulapalli Nandu Navadeep>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
