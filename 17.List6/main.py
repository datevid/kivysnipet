from datetime import datetime
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
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, ILeftBodyTouch
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox
from Service import ActiviItem, ActiviService


class DataModalTmp():
    """para guardar dato elegido en el modal como el valor completo de la fecha"""

    # almacenamos datetime
    dialogNewActiviDateTime = None;


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
    # shopItem = ObjectProperty()
    pkId = NumericProperty()

    def __int__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk

    def mark(self, check, itemkvId, pkId):
        "marca si está completado o por completar"
        print(f"itemkvId {itemkvId}, pkId {pkId}")
        if (check.active):
            print("activo")
            itemkvId.text = f'[s]{itemkvId.text}[s]'
        else:
            print("inactivo")

    def deleteItem(self, itemkvId):
        print(itemkvId)
        self.parent.remove_widget(itemkvId)


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    "checkbox de la lista principal"


class ListApp(MDApp):
    # lista de actividades se almacenan en esta variable
    activiData = None;

    # almacenamos el objeto modal
    dialogNewActivi = None;

    # almacenamos datos temporales como datetime del modal
    dataModalTmp: DataModalTmp() = DataModalTmp();

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("List App 0")
        # self.loadData();
        self.loadData();

    def loadData(self):
        print("Load data")
        # set data icons
        icons = list(md_icons.keys())

        # add values to shoppinList
        self.activiData: ActiviService = ActiviService();
        for i in range(5):
            id = i + 1
            date = datetime.now()
            self.activiData.addItem(ActiviItem(i + 1, f"item co id {id}", icons[i], date))

    def build(self):
        # self.theme_cls.primary_palette = "Orange"
        # self.theme_cls.theme_style = "Dark"
        # return Builder.load_file("main.kv")
        screen = Builder.load_file("main.kv")
        print("List App 1")
        self.title = "LionAPP"
        return InterfazMain();

    def on_start(self):
        print("List App 2")

        # render items of list main
        self.renderActiviAll();

    def renderActiviAll(self):
        for i in range(len(self.activiData.getList())):
            activiItem = self.activiData.getList()[i];
            self.renderActiviOne(activiItem);

    def renderActiviOne(self, activiItem: ActiviItem):
        self.root.ids.scroll.add_widget(
            ItemWithCheckbox(
                text=activiItem.name,
                icon=activiItem.icon,
                pkId=activiItem.id,
                # shopItem=self.activiList.getItem(i),
                # on_press=self.on_click_item
                on_press=partial(self.onSelectedItemActivi, activiItem)
            )
        )

    def renderActiviLast(self):
        """Actualiza el ultimo item adicionado a la lista.
        Detalle:
        Cuando se actualiza la lista dinámica,
        en el render sólo se actualizará el último adicionado
        para evitar pintar tudo de nuevo
        """
        activiItem = self.activiData.getList()[-1]
        self.renderActiviOne(activiItem);

    def openDialogNewActivi(self):
        print("agregar item a la lista principal")
        # if not self.flagDialogNewActivi:
        self.dialogNewActivi = MDDialog(
            title="Nueva actividad",
            type="custom",
            content_cls=DialogContentNewActivi()
        )
        self.dialogNewActivi.open();

    def closeDialogNewActivi(self):
        self.dialogNewActivi.dismiss();

    def addNewActivi(self, activiDialogNameKvId, activiDialogDateKvId):
        print(f"nueva actividad name:{activiDialogNameKvId.text} date {activiDialogDateKvId.text}")
        # self.activiList.addItem(ActiviItem(5 + 1, activiDialogNameKvId.text, date))
        next_value = self.activiData.getSequence();
        activiItemNew = ActiviItem(next_value, activiDialogNameKvId.text, "android",
                                   self.dataModalTmp.dialogNewActiviDateTime)
        self.activiData.addItem(activiItemNew)
        self.renderActiviLast();

    def save_cust_to_db(self):
        print(self.root.ids.nombre_input.text)

    def on_click_item(self, widget):
        print("-----")
        print('wdiget:', widget);
        print('wdiget.text:', widget.text);

    # https://stackoverflow.com/questions/64658165/how-to-add-on-press-function-on-a-onelineavatariconlistitem-added-from-main-py
    # https://stackoverflow.com/questions/69620701/adding-labels-for-each-onelineavatarlistitem-python-kivy
    # https://stackoverflow.com/questions/39809206/kivy-python-passing-parameters-to-fuction-with-button-click
    # https://www.reddit.com/r/kivy/comments/pecyjb/how_do_i_add_multiple_functions_to_on_press/
    # https://stackoverflow.com/questions/19796866/python-how-to-bind-button-on-press-on-kivy-with-multiple-parameters
    def onSelectedItemActivi(self, activiItem: ActiviItem, widget):
        """
        Al seleccionar un item de la lista de actividades
        :param activiItem:
        :param widget: siempre está al final
        :return:
        """
        print("-----")
        print('activiItem:', activiItem);
        print('wdiget:', widget);
        print('wdiget.text:', widget.text);


class DialogContentNewActivi(MDBoxLayout):
    "Abre el diálogo para nueva actividad"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        date = datetime.now().strftime('%A %d %B %Y')
        self.ids.activiDialogDate.text = str(date)

    def showDatePickerNewActivi(self):
        dateDialog = MDDatePicker();
        dateDialog.bind(on_save=self.on_save)
        dateDialog.open();

    def on_save(self, instance, dateValue, date_range):
        """This functions gets the date from the date picker and converts its it a
        more friendly form then changes the date label on the dialog to that"""
        print("hla mundo fecha:", dateValue)
        print("RANGO:", date_range)
        date = dateValue.strftime('%A %d %B %Y')
        self.ids.activiDialogDate.text = str(date)

        # valor de la fecha sin formato y guardado para ser usado posteriormente
        self.dataModalTmp.dialogNewActiviDateTime = dateValue;


if __name__ == '__main__':
    ListApp().run();
