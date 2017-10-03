from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 


from kivymd.theming import ThemeManager
import os

from login import Login
from principal import Principal

class MeuApp(App): 
    theme_cls = ThemeManager()
    def build(self): 
        manager = ScreenManager() 
        manager.add_widget(Login(name='login'))
        manager.add_widget(Principal(name='principal'))
        
        return manager 
 
if   __name__  == '__main__': 
    MeuApp().run() 