
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import os
kivy.require('1.9.1')


class Team(Widget):
    num = NumericProperty()
    name = StringProperty()


class TeamScreen(Screen):
    num = NumericProperty()


class TeamsScreen(Screen):
    def do_layout(self, *args):
        numbers = []
        file = open(os.getcwd() + '/teams.txt', 'r')
        for line in file.readlines():
            split = line.split("|")
            numbers.append((int(split[0]), str(split[1])))
        print "Team numbers: ", numbers
        for num, name in numbers:
            self.ids.team_grid.add_widget(Team(num=num, name=name))
        self.ids.team_grid.rows = len(numbers)


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
