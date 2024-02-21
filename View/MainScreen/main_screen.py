from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


class SmallCard(MDCard):
    shape = StringProperty("None")
    inputs = StringProperty("None")
    outputs = StringProperty("None")
    imagepath = StringProperty("None")
    constant = 2.65
    medium = 425/constant
    large = 478/constant
    # 2.65


class MainScreenView(Screen):
    pass
