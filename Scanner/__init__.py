from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

class InitialScreen(Screen):
    pass
class SubnetInput(Screen):
    def get_input(self, text_inputs):
            input_ip = text_inputs[0].text
            input_subnet = text_inputs[1].text
            print(input_ip,input_subnet)
    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""
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
    def get_input(self, text_input):
        input_ip = text_input.text
        print(input_ip)
    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""
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
