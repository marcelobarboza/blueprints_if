#!/usr/bin/env python3

import os
import npyscreen


class Blueprints(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm('MAIN', MainForm())


class MainForm(npyscreen.Form):
    def create(self):
        self.name = self.add(
                npyscreen.TitleText,
                name='Professor',
                value='Marcelo Barboza'
                )
        self.date = self.add(npyscreen.TitleDateCombo, name='Data')
        data = [
                dirs for dirs, subdirs, files in os.walk('pkgs/plano/')
                if dirs != 'pkgs/plano/' and '__pycache__' not in dirs
                ]
        self.fold = self.add(
                npyscreen.TitleMultiSelect,
                max_height=-2,
                name='Planos',
                values=data,
                scroll_exit=True
                )

    def afterEditing(self):
        self.parentApp.setNextForm(None)


if __name__ == '__main__':
    app = Blueprints()
    app.run()
