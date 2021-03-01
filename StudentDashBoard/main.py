import webbrowser
import datetime
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


class MainWindow(Screen):
    def openMoodle(self):
        webbrowser.open_new_tab("https://students.iitmandi.ac.in/moodle/my")

class Todo(Screen):
    pass

class SecondWindow(Screen):
    pass

class Cisco(Screen):
    pass
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("final.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()