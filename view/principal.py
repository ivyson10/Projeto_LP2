from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.theming import ThemeManager
from kivy.app import App
from model.crud_vendedor import pesquisa_vendedor, delete_vendedor,pesquisa_vendedor_all,update_vendedor
from kivy.properties import ObjectProperty




Builder.load_file('view/principal.kv') 

class Principal(Screen):
    
    def pesquisa_ven(self,cpfText):
        app = App.get_running_app()
        app.cpf = cpfText
        ven_lista = pesquisa_vendedor(app.cpf)
        print(ven_lista)


    def deleta_ven(self, idText):
        app = App.get_running_app()
        app.id = idText
        delete_vendedor(app.id)
        lista = pesquisa_vendedor_all()
        for row in lista:
            print(row)

    def update_ven(self, idText):
        app = App.get_running_app()
        app.ided = idText
        update_vendedor(app.ided)
        lista = pesquisa_vendedor_all()
        for row in lista:
            print(row)