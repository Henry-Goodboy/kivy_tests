import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label #we will always import something with kivy!

class MyApp(App):
    def build(self):
        input('Write Something: ')
        return Label(text="Hello World")
    
MyApp().run()
