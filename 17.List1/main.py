from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox

class Screen1(Screen):
    pass
class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class ContentNavigationDrawer(Screen):
    #screen_manager = ObjectProperty()
    #nav_drawer = ObjectProperty()
    pass

class InterfazMain(ScreenManager):
    def listclick(self):
        print("hola item")
    
    pass


class Example(MDApp):
    def build(self):
        #self.theme_cls.primary_palette = "Orange"
        #self.theme_cls.theme_style = "Dark"
        #return Builder.load_file("main.kv")
        screen = Builder.load_file("main.kv")
        return InterfazMain();
    
    


Example().run()