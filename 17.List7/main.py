from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox

Builder.load_file("main.kv")


class Screen1(Screen):
    pass


class Screen2(Screen):
    pass


class Screen3(Screen):
    pass


class InterfazWithScreen1(Screen):
    navDrawerId = ObjectProperty()
    screenManagerId = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("List App InterfazWithScreen1")

    def listclick(self):
        print("hola item")

    def changeScreenInner(self, screenName):
        """ inner of screen"""
        self.ids.screenManagerId.current=screenName


class WindowManager(ScreenManager):
    pass


class Example(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("List App 0")

    def build(self):

        self.wm=WindowManager()
        screens=[
            InterfazWithScreen1(name="interfaz"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        self.wm.current="interfaz"
        return self.wm;

Example().run()