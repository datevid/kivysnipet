from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

Builder.load_file("main.kv")


class ScreenInner1(MDScreen):
    pass


class ScreenInner2(MDScreen):
    pass


class ScreenInner3(MDScreen):
    pass


class ScreenWithMenu(MDScreen):
    pass


class ScreenWithoutMenu(MDScreen):
    pass


class ScreenNavigationMain(MDScreen):
    navDrawerId = ObjectProperty()
    screenInnerId = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WindowManager(ScreenManager):
    pass


class ExampleDatevid(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.wm = WindowManager()
        screens = [
            ScreenNavigationMain(name="screenNavigationMain"),  # self.wm.screens[0]
            ScreenWithoutMenu(name="screenWithoutMenu"),  # self.wm.screens[1]
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        # self.wm.current="interfaz"

        # charge screen inners in screenwrapper main
        self.screenInnerBuilder();

        return self.wm;

    def screenInnerBuilder(self):
        """charge screen inners in screenWrapper"""
        screenInner1 = ScreenInner1(name="scr1")
        screenInner2 = ScreenInner2(name="scr2")
        screenInner3 = ScreenInner3(name="scr3")
        screenWithMenu = ScreenWithMenu(name="ScreenWithMenu")
        self.wm.screens[0].ids['screenInnerId'].add_widget(screenInner1);
        self.wm.screens[0].ids['screenInnerId'].add_widget(screenInner2);
        self.wm.screens[0].ids['screenInnerId'].add_widget(screenInner3);
        self.wm.screens[0].ids['screenInnerId'].add_widget(screenWithMenu);

    def changeScreen(self, screen):
        self.wm.current = screen;

    def changeScreenInner(self, screenInnerName):
        """
        No funciona si usa Button o  elementos de solo kivy
        Debe usar kivyMD para ver el correcto funcionamiento.
        :param screenInnerName:
        :return:
        """
        print(f"Cambiando screen Inner {screenInnerName}")
        self.wm.screens[0].ids['screenInnerId'].current = screenInnerName;

    def listclick1(self):
        print("hola item1")

    def listclick2(self):
        print("hola item2")

    def onClicScreenWithMenu(self):
        """ tambien puede usar changeScreenInner()"""
        self.wm.screens[0].ids['screenInnerId'].current = "ScreenWithMenu";

    def onClicScreenWithoutMenu(self):
        """ tambien puede usar changeScreen()"""
        self.wm.current = "screenWithoutMenu";


if __name__ == '__main__':
    ExampleDatevid().run();

