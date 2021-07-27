from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

class InitialScreen(Screen):
    pass
class SubnetInput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
    def back(self,window,key,*args):
        if key == 27: #esc key
            App.get_running_app().root.current = 'Home'
            return True
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
class ScanOutput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
    def back(self,window,key,*args):
        if key == 27: #esc key
            App.get_running_app().root.current = 'Home'
            return True
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
class SSHInput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
    def back(self,window,key,*args):
        if key == 27: #esc key
            App.get_running_app().root.current = 'Home'
            return True
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
class SSHOutput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
    def back(self,window,key,*args):
        if key == 27: #esc key
            App.get_running_app().root.current = 'Home'
            App.transition= "Right"
            return True
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
class WindowManager(ScreenManager):
    pass
    
kv=Builder.load_file("./Scanner/design/Design.kv")
class IpScanner(App):
    def build(self):
        return kv
