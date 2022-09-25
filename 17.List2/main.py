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
    pass

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class Example(MDApp):
    def build(self):
        #self.theme_cls.primary_palette = "Orange"
        #self.theme_cls.theme_style = "Dark"
        #return Builder.load_file("main.kv")
        screen = Builder.load_file("main.kv")
        return InterfazMain();
    
    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(30):
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=f"Item {i}", icon=icons[i])
            )


Example().run()