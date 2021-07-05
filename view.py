from re import MULTILINE
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

class IpScanner(App):
    def build(self):
        Window.clearcolor = (0.039, 0.039, 0.039, 1)
        self.InitialScreen = GridLayout()
        self.InitialScreen.cols = 1
        
        self.InitialScreen.size_hint = (0.6, 0.7)
        self.InitialScreen.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.InitialScreen.add_widget(Image(source="filler.png"))
        self.SubnetID = Label(text='This is a potato: ',
                              font_size=20, color="#FAD02C")
        self.InitialScreen.add_widget(self.SubnetID)
        self.SubnetID_input = TextInput(hint_text="Subnet I.D, e.g. 192.168.0.0",multiline=False,padding=("10dp","10dp","5dp","10dp"),size_hint=(0.6,0.3),background_color="#E5E8E8")
        self.InitialScreen.add_widget(self.SubnetID_input)
        self.SubnetID_input = TextInput(hint_text="Subnet mask, e.g. 255.255.255.0 ",multiline=False,padding=("10dp","10dp","5dp","10dp"),size_hint=(0.6,0.3),background_color="#E5E8E8")
        self.InitialScreen.add_widget(self.SubnetID_input)
        self.Scan_button = Button(text='Scan',bold=True,size_hint=(0.6,0.3),background_color="#949494")
        self.InitialScreen.add_widget(self.Scan_button)
        return self.InitialScreen

    def callback(self, instance):
        pass
if __name__ == "__main__":
    IpScanner().run()
