from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 


from kivymd.theming import ThemeManager
import os

from view.login import Login
from view.principal import Principal
from view.cadastrocliente import CadastroCliente
from view.cadastrovendedor import CadastroVendedor
from view.cadastrofornecedor import CadastroFornecedor


class MeuApp(App): 
    theme_cls = ThemeManager()
   
    def build(self):
        manager = ScreenManager() 
        manager.add_widget(Login(name='login'))
        manager.add_widget(Principal(name='principal'))
        manager.add_widget(CadastroCliente(name='cadastrocliente'))
        manager.add_widget(CadastroVendedor(name='cadastrovendedor'))
        manager.add_widget(CadastroFornecedor(name='cadastrofornecedor')) 
        return manager
def main():
    MeuApp().run()
if   __name__  == '__main__': 
    main() 