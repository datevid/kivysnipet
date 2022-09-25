from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
    
    

#Builder.load_file("main.kv")

class ContentMenu(Screen):
    #para compartir las propiedades,
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass


class InterfazMain(ScreenManager):
    pass

class TestApp(MDApp):
    def build(self):
        screen = Builder.load_file("main.kv")
        #return screen;
        return InterfazMain()

if __name__ == '__main__':
    TestApp().run();
