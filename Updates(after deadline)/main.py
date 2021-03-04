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
    day = StringProperty(str(datetime.datetime.today().weekday()+1))
    def openMoodle(self):
        webbrowser.open_new_tab("https://students.iitmandi.ac.in/moodle/my")

class Todo(Screen):
    pass

class SecondWindow(Screen):
    pass

class Cisco(Screen):
    pass

class Monday(Screen):
    def ic252(self):
        #webbrowser.open_new_tab("
        pass

    def ic111(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=mce838d21e53aa13df650b63777b45119")

    def ic141(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=md5e1ff269f509e2860d5f4428b0f9ac7")

    def ic140(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m6a8cd01030cd80d3920ca01097133aef")

    def hs342(self):
        #webbrowser.open_new_tab("
        pass



class Tuesday(Screen):
    def ic252(self):
        #webbrowser.open_new_tab("")
        pass

    def hs342(self):
        #webbrowser.open_new_tab("
        pass

    def ic152(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m5b91f8ee963ff2413934df8642a4afb9")

    def hs106(self):
        webbrowser.open_new_tab("https://meet.google.com/kyh-cous-sho")


class Wednesday(Screen):
    def ic111(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=me13febe6d7966531d7d8d5616b28512d")

    def ic141(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m0ee82f226853351516f3d8f8c8ca1762")

    def ic140(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m6a8cd01030cd80d3920ca01097133aef")

    def ic152(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=mba7de49892a04d1fd21e5411900d6132")



class Thursday(Screen):
    def ic252(self):
        #webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m19d47ffbef23243b6ce23482130606a0")
        pass

    def ic111(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m89997387f53a518a601b01859389b9c3")

    def hs342(self):
        #webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m19d47ffbef23243b6ce23482130606a0")
        pass

    def ic152(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m19d47ffbef23243b6ce23482130606a0")

    def hs106(self):
        webbrowser.open_new_tab("https://meet.google.com/kyh-cous-sho")



class Friday(Screen):
    def ic152p(self):
        webbrowser.open_new_tab("https://iitmandi.webex.com/iitmandi/j.php?MTID=m0cb8ff927ec58793582cadc6c067c5f0")

    def hs106(self):
        webbrowser.open_new_tab("https://meet.google.com/kyh-cous-sho")



class Chill(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("final.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()