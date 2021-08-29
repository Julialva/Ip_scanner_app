from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from Scanner.features.ssh import socket_test


class InitialScreen(Screen):
    pass


class SubnetInput(Screen):
    def get_input(self, text_inputs):
        App.get_running_app().MY_SUBNET = text_inputs[0].text
        App.get_running_app().MY_MASK = text_inputs[1].text
        # print(App.get_running_app().MY_SUBNET,App.get_running_app().MY_MASK)
        return

    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""
        return

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
        return

    def back(self, window, key, *args):
        if key == 27:  # esc key
            App.get_running_app().root.current = "Home"
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return


class ScanOutput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
        return

    def back(self, window, key, *args):
        if key == 27:  # esc key
            App.get_running_app().root.current = "Home"
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return


class SSHInput(Screen):
    def get_input(self, text_input):
        App.get_running_app().MY_IP = text_input.text
        return

    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""
        return

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
        return

    def back(self, window, key, *args):
        if key == 27:  # esc key
            App.get_running_app().root.current = "Home"
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return


class SSHOutput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
        return

    def back(self, window, key, *args):
        if key == 27:  # esc key
            App.get_running_app().root.current = "Home"
            App.transition = "Right"
            return True

    def ssh_test(self):
        self.ids.SSHresult.text = App.get_running_app().SSH_STATUS = socket_test(
            App.get_running_app().MY_IP, port=22
        )
        return

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("./Scanner/design/Design.kv")


class IpScanner(App):
    MY_IP = ""
    MY_SUBNET = ""
    MY_MASK = ""

    def build(self):
        return kv
