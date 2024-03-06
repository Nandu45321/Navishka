from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem


class SmallCard(MDCard):
    shape = StringProperty("None")
    inputs = StringProperty("None")
    outputs = StringProperty("None")
    imagepath = StringProperty("None")
    constant = 2.65
    medium = 425 / constant
    large = 478 / constant
    # 2.65


class MainScreenView(Screen):

    def on_switch_tabs(
            self,
            bar: MDNavigationBar,
            item: MDNavigationItem,
            item_icon: str,
            item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text
