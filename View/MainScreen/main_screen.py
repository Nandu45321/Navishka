from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar
from kivymd.uix.screen import MDScreen


class SmallCard(MDCard):
    shape = StringProperty("None")
    inputs = StringProperty("None")
    outputs = StringProperty("None")
    imagepath = StringProperty("None")
    constant = 2.65
    medium = 425 / constant
    large = 478 / constant
    # 2.65


print("""    Navishka
    Copyright (C) 2024  Yamulapalli Nandu Navadeep

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or 
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.""")


class DNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class TwoDScreen(MDScreen):
    ...


class ThreeDScreen(MDScreen):
    ...


class MainScreenView(Screen):

    def on_switch_tabs(
            self,
            bar: MDNavigationBar,
            item: MDNavigationItem,
            item_icon: str,
            item_text: str, ):
        self.ids.entry_screen_manager.current = item_text
