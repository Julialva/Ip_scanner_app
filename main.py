from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class IpWindow(Widget):
    pass
class IpScanner(App):
    def build(self):
        Window.clearcolor=(0.58,0.79,0.45,1)
        return IpWindow()


if __name__ == "__main__":
    IpScanner().run()
