from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("main5.kv")

class Mi(Screen):
    pass

class TestApp(MDApp):
    def build(self):
        sm = ScreenManager();
        sm.add_widget(Mi(name='screen1'))
        return sm;

if __name__ == '__main__':
    TestApp().run();
