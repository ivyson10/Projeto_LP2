from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.theming import ThemeManager
from kivy.app import App
from model.crud_vendedor import pesquisa_vendedor
from kivy.properties import ObjectProperty



Builder.load_file('view/principal.kv') 

class Principal(Screen):
    
    def pesquisa_ven(self,cpfText):
        input_ven = ObjectProperty()
        app = App.get_running_app()
        app.cpf = cpfText
        ven_lista = pesquisa_vendedor(app.cpf)
        print(ven_lista)
        self.manager.get_screen('principal').add_widget(input_ven(text=str(ven_lista)))