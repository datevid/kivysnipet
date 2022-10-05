from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kv = """
<ScreenMain>:
    BoxLayout:
        Button:
            text: "Access label"
            #on_press: root.access_label()
            on_press: app.access_label()
        MyWidget:
            id: my_widget


<MyWidget>
    Label:
        id: my_label
        text: "not yet accessed"
"""

Builder.load_string(kv)
class MyWidget(BoxLayout):
    pass

class ScreenMain(Screen):
   """"""

class WindowManager(ScreenManager):
    pass

class TestApp(App):
    def build(self):
        self.wm = WindowManager()
        screens = [
            ScreenMain(name="interfaz"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        self.wm.current='interfaz'
        return self.wm;

    def access_label(self):
        #self.ids.my_widget.ids.my_label.text = 'Accessed!'
        print(self.wm.screens[0].ids.my_widget.ids.my_label.text)
        self.wm.screens[0].ids.my_widget.ids.my_label.text = "Accedido"


if __name__ == '__main__':
    TestApp().run()