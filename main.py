
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.9.1')


class Team(Widget):
    num = NumericProperty()


class TeamScreen(Screen):
    pass


class TeamsScreen(Screen):
    num = NumericProperty()


class ScoutScreenManager(ScreenManager):
    def goto_team(self, n):
        s = TeamScreen(num=n, name=str(n))
        self.add_widget(s)
        self.current = str(n)


class ScoutApp(App):
    def build(self):
        return ScoutScreenManager()


if __name__ == '__main__':
    ScoutApp().run()
