'''
Application example using build() + return
==========================================

An application can be built if you return a widget on build(), or if you set
self.root.
'''

import kivy

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        # return a Button() as a root widget
        return Button(text='hello AlexP')


MyApp().run()
# if __name__ == '__main__':
# MyApp().run()
