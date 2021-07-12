from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class InitialScreen(Screen):
    pass
class SubnetInput(Screen):
    pass
class ScanOutput(Screen):
    pass
class SSHInput(Screen):
    pass
class SSHOutput(Screen):
    pass
class WindowManager(ScreenManager):
    pass
    
kv=Builder.load_file("./Scanner/design/Design.kv")
class IpScanner(App):
    def build(self):
        return kv
