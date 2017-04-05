
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
        s = TeamScreen(num=n, name="Team name")
        self.add_widget(s)
        self.current = "Team name"
    ###############################################################################
    # def do_layout(self, *args):                                                 #
    #     super(ScoutLayout, self).do_layout()                                    #
    #     layout = self.ids['layout']                                             #
    #     # self.ids.layout.bind(minimum_height=self.ids.layout.setter('height')) #
    #     layout.bind(minimum_height=layout.setter('height'))                     #
    #     print layout.minimum_height                                             #
    ###############################################################################


class ScoutApp(App):
    def build(self):
        return ScoutScreenManager()


if __name__ == '__main__':
    ScoutApp().run()
