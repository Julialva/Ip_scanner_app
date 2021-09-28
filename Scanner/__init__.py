from datetime import date
from time import sleep

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from Scanner.features.ssh import socket_test
from Scanner.features.sweeper import sweeper
from Scanner.features.utility import format_df, is_ip, list_in_caps


class InitialScreen(Screen):
    pass


class SubnetInput(Screen):
    def get_input(self, text_inputs):
        MDApp.get_running_app().MY_SUBNET = text_inputs[0].text
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
            MDApp.get_running_app().root.current = "Home"
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return

    def validate_ip(self, addr):
        return is_ip(addr.text)


class ScanOutput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
        return

    def back(self, window, key, *args):
        if key == 27:  # esc key
            MDApp.get_running_app().root.current = "Home"
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return

    def on_enter(self, *args):
        MDApp.get_running_app().DF = sweeper(MDApp.get_running_app().MY_SUBNET).run()
        columns_data, rows_data = format_df(MDApp.get_running_app().DF)
        columns_data = list_in_caps(columns_data)
        columns_data = [(x, dp(60)) for x in columns_data]
        table = MDDataTable(
            column_data=columns_data,
            row_data=rows_data,
            use_pagination=True,
        )
        MDApp.get_running_app().AUX = False
        self.add_widget(table)


class SSHInput(Screen):
    def get_input(self, text_input):
        MDApp.get_running_app().MY_IP = text_input.text
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
            MDApp.get_running_app().root.current = "Home"
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return

    def validate_ip(self, addr):
        return is_ip(str(addr))


class SSHOutput(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)
        return

    def back(self, window, key, *args):
        if key == 27:  # esc key
            MDApp.get_running_app().root.current = "Home"
            MDApp.transition = "Right"
            return True

    def ssh_test(self):
        self.ids.SSHresult.text = MDApp.get_running_app().SSH_STATUS = socket_test(
            MDApp.get_running_app().MY_IP, port=22
        )
        return

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back)
        return


class WindowManager(ScreenManager):
    pass


class IpScanner(MDApp):
    MY_IP = ""
    MY_SUBNET = ""
    DF = None
    AUX = True

    def build(self):
        kv = Builder.load_file("./Scanner/design/Design.kv")
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "700"
        return kv
