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


class TwoDNavigationItem(MDNavigationItem):
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
