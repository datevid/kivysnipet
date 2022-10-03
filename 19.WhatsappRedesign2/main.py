from functools import partial

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty, DictProperty, OptionProperty, BooleanProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox
from Service import ShoppingItem, ShoppingList
from demo.demo import profiles

Window.size=(320,600)
Builder.load_file("main.kv")
Builder.load_file("pages/story.kv")
Builder.load_file("pages/ChatListItem.kv")
Builder.load_file("pages/chatScreen.kv")
Builder.load_file("pages/text_field.kv")

class Screen1(Screen):
    pass


class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class WindowManager(ScreenManager):
    """Window manager"""

class MessageScreen(Screen):
    """display the stories and all message histories"""

class StoryWithImage(MDBoxLayout):
    """ horizontal layout with image"""
    text=StringProperty() #to store username
    source=StringProperty()# the path to the user picture

class ChatScreen(Screen):
    '''A screen that display messages with a user.'''
    text = StringProperty()
    image = ObjectProperty()
    active = BooleanProperty(defaultvalue=False)

class ChatListItem(MDCard):
    """ A clickable chat item for the chat timeline"""
    mssg = StringProperty()  # to store username
    friend_avatar = StringProperty()  # the path to the user picture
    timestamp = StringProperty()  # time the message was sent
    profile = DictProperty()  # An user from demo.profile
    isRead = OptionProperty(
        None, options=['delivered','read','new','waiting']
    )
    friend_name=StringProperty()


class ListApp(MDApp):
    def build(self):
        self.title="Whatsapp rediseño"

        screens=[
            MessageScreen(name="message"),
            ChatScreen(name="chat-screen")
        ]
        self.wm=WindowManager(transition=FadeTransition())
        for screen in screens:
            self.wm.add_widget(screen);

        self.storyBuilder();
        self.chatListBuilder();

        #setting current screen
        #self.wm.current="message"
        #self.wm.current="chat-screen"

        return self.wm;

    def storyBuilder(self):
        """Create a story for each user and add it to the story layout"""
        for profile in profiles:
            self.story=StoryWithImage()
            self.story.text=profile['name']
            self.story.source=profile['image']
            self.wm.screens[0].ids['story_layout'].add_widget(self.story)

    def chatListBuilder(self):
        """Create a chat list item for each user and add it to message list"""
        for messages in profiles:
            for message in messages['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = messages
                self.chatitem.friend_name = messages['name']
                self.chatitem.friend_avatar = messages['image']

                lastmessage, time, isRead, sender = message.split(';')
                self.chatitem.mssg = lastmessage
                self.chatitem.timestamp = time
                self.chatitem.isRead = isRead
                self.chatitem.sender = sender
            self.wm.screens[0].ids['chatTimeline'].add_widget(self.chatitem)

    def change_screen(self,screen):
        self.wm.current=screen

    def create_chat(self, profile):
        '''Get all messages and create a chat screen'''
        self.chat_screen = ChatScreen()
        #self.msg_builder(profile, self.chat_screen)
        self.chat_screen.text = profile['name']
        self.chat_screen.image = profile['image']
        self.chat_screen.active = profile['active']
        self.wm.switch_to(self.chat_screen)

if __name__ == '__main__':
    ListApp().run();
