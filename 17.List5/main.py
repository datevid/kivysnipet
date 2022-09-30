from functools import partial

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty, NumericProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, ILeftBodyTouch
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
    """
    Pantala principal donde se muestra:
    -Menu de navegación
    -Barra de menú
    -Screen1: lista de actividades
    -boton para adicionar un item a la lista de actividades
    """



class ItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    # see https://snyk.io/advisor/python/Kivy/functions/kivy.properties.StringProperty
    icon = StringProperty("android")
    text2 = StringProperty()
    # shopLst = ListProperty()
    shopItem = ObjectProperty()
    pkId = NumericProperty()
    # text=shopItem.name


    def __int__(self,pk=None,**kwargs):
        super().__init__(**kwargs)
        self.pk=pk

    def mark(self,check,itemkvId,pkId):
        "marca si está completado o por completar"
        print(f"itemkvId {itemkvId}, pkId {pkId}")
        if(check.active):
            print("activo")
            itemkvId.text=f'[s]{itemkvId.text}[s]'
        else:
            print("inactivo")

    def deleteItem(self,itemkvId):
        print(itemkvId)
        self.parent.remove_widget(itemkvId)


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class LeftCheckbox(ILeftBodyTouch,MDCheckbox):
    "checkbox de la lista principal"


class ListApp(MDApp):
    icons=[];
    listaActividades=[];

    def __int__(self):
        print("List App 0")

    def loadData(self):
        # set data icons
        self.icons = list(md_icons.keys())

        # add values to shoppinList
        self.listaActividades: ShoppingList = ShoppingList();
        for i in range(30):
            id = i + 1
            self.listaActividades.addItem(ShoppingItem(i + 1, f"item co id {id}", self.icons[i]))
        pass

    def build(self):
        # self.theme_cls.primary_palette = "Orange"
        # self.theme_cls.theme_style = "Dark"
        # return Builder.load_file("main.kv")
        screen = Builder.load_file("main.kv")
        print("List App 1")
        return InterfazMain();

    def on_start(self):
        print("List App 2")

        #load data
        self.loadData();

        # render items of list main
        for i in range(30):
            self.root.ids.scroll.add_widget(
                ItemWithCheckbox(
                    text=self.listaActividades.getItem(i + 1).name,
                    icon=self.icons[i],
                    shopItem=self.listaActividades.getItem(i + 1),
                    pkId=self.listaActividades.getItem(i + 1).id,
                    on_press=self.on_click_item
                    #on_press=partial(self.my_function, 'btn1')

                )
            )

    def addNewItemToMain(self):
        print("agregar item a la lista principal")

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
