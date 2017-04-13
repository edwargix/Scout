
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, DictProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

import os
import json

kivy.require('1.9.1')


teams = {}


class Team(Widget):
    num = StringProperty()
    name = StringProperty()


class TeamScreen(Screen):
    num = StringProperty()
    values = DictProperty()


class TeamsScreen(Screen):
    def do_layout(self, *args):
        self.ids.team_grid.rows = len(teams)
        for team in sorted(teams.iterkeys()):
            self.ids.team_grid.add_widget(Team(num=team, name=teams[team]['name']))


class ScoutScreenManager(ScreenManager):
    def goto_team(self, n):
        s = TeamScreen(num=n, name=str(n), values=teams[str(n)])
        self.add_widget(s)
        self.current = str(n)

    def save_team(self, n, values):
        print 'Saving data for team ', n
        old_name = teams[n]['name']
        teams[n] = values
        teams[n]['name'] = old_name

        with open('data.txt', 'w') as file:
            file.write(json.dumps(teams))
            print 'team! ', teams[n]


class ScoutApp(App):
    def build(self):
        global teams
        try:
            with open('data.txt', 'r') as file:
                teams = json.loads(file.read())
        finally:
            print teams
            with open('teams.txt', 'r') as file:
                for line in file.readlines():
                    split = line.split('|')
                    num = split[0]
                    name = split[1][:-1]
                    if num not in teams:
                        print 'this thing ran!', num, name
                        teams[num] = {
                            'name': split[1][:-1],
                            'auto': [False, False, False],
                            'notes': '',
                            'teleop': {
                                'gears': '',
                                'high goal': '',
                                'defense': ''
                            }
                        }
                    else:
                        teams[num]['name'] = name

            return ScoutScreenManager()


if __name__ == '__main__':
    ScoutApp().run()
