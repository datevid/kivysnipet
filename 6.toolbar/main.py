from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

Window.size=(480,800)
Builder.load_file("main.kv")

class Screen1(Screen):
    pass
    

class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Amber"
        #self.theme_cls.primary_palette="Purple"
        sm = ScreenManager();
        sm.add_widget(Screen1(name='screen1'))
        return sm;
    
    def fnMenu(self):
        print("hola menuRoot")

if __name__ == '__main__':
    TestApp().run();
