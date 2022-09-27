from functools import partial

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox
from Service import ShoppingItem, ShoppingList


class Screen1(Screen):
    pass


class Screen2(Screen):
    pass


class Screen3(Screen):
    pass


class ContentNavigationDrawer(Screen):
    # screen_manager = ObjectProperty()
    # nav_drawer = ObjectProperty()
    pass


class InterfazMain(ScreenManager):
    pass


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    # see https://snyk.io/advisor/python/Kivy/functions/kivy.properties.StringProperty
    icon = StringProperty("android")
    text2 = StringProperty()
    #shopLst = ListProperty()
    shopItem=ObjectProperty()
    #text=shopItem.name


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class ListApp(MDApp):
    def build(self):
        # self.theme_cls.primary_palette = "Orange"
        # self.theme_cls.theme_style = "Dark"
        # return Builder.load_file("main.kv")
        screen = Builder.load_file("main.kv")
        return InterfazMain();

    def on_start(self):
        # set data icons
        icons = list(md_icons.keys())

        # add values to shoppinList
        shopLst = ShoppingList();
        for i in range(30):
            shopLst.addItem(ShoppingItem(i+1, f"itemcito {i}", icons[1]))
        #print(shopLst)
        print(shopLst.getItem(1))
        
        # render
        for i in range(30):
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(
                    #text=f"Item1111 {i}",
                    text=shopLst.getItem(i+1).name,
                    icon=icons[i],
                    shopItem=shopLst.getItem(i+1),
                    on_press=self.on_click_item
                    #on_press=partial(self.my_function, 'btn1')

                )
            )

    def save_cust_to_db(self):
        print(self.root.ids.nombre_input.text)
    
    def on_click_item(self,widget):
        print("-----")
        print('wdiget.text:', widget.text);

    #https://stackoverflow.com/questions/64658165/how-to-add-on-press-function-on-a-onelineavatariconlistitem-added-from-main-py
    #https://stackoverflow.com/questions/69620701/adding-labels-for-each-onelineavatarlistitem-python-kivy
    #https://stackoverflow.com/questions/39809206/kivy-python-passing-parameters-to-fuction-with-button-click
    #https://www.reddit.com/r/kivy/comments/pecyjb/how_do_i_add_multiple_functions_to_on_press/
    #https://stackoverflow.com/questions/19796866/python-how-to-bind-button-on-press-on-kivy-with-multiple-parameters
    def my_function(self,widget,var1):
        print("-----")
        print('wdiget.text:', widget);
        print('var1:', var1);



if __name__ == '__main__':
    ListApp().run();
