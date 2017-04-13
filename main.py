
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
import json

kivy.require('1.9.1')


teams = {}


class Team(Widget):
    num = NumericProperty()
    name = StringProperty()


class TeamScreen(Screen):
    num = NumericProperty()


class TeamsScreen(Screen):
    def do_layout(self, *args):
        numbers = []
        teams_file = open(os.getcwd() + '/teams.txt', 'r')
        for line in teams_file.readlines():
            split = line.split("|")
            numbers.append((int(split[0]), str(split[1])))
        print "Team numbers: ", numbers
        self.ids.team_grid.rows = len(numbers)
        for num, name in numbers:
            self.ids.team_grid.add_widget(Team(num=num, name=name))


class ScoutScreenManager(ScreenManager):
    def goto_team(self, n):
        s = TeamScreen(num=n, name=str(n))
        self.add_widget(s)
        self.current = str(n)

    def save_team(self, n):
        print 'Saving data for team ', n
        done = False
        # Format:
        # [match numbers],[bool,bool,bool],"Notes",["teleop"]
        try:
            with open('data.txt', 'r') as read_data:
                for line in read_data.readlines():
                    print 'Line: ', line
                    split = line.split('|')
                    if (split[0] == str(n)):
                        # TODO: change data for team
                        done = True
                        break
            if (done == False):
                print 'Attempting to append data'
                with open('data.txt', 'a') as append_data:
                    append_data.write('\n' + str(n) + '|')
        except IOError:
            with open('data.txt', 'w') as data:
                data.write(str(n) + '|')


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
