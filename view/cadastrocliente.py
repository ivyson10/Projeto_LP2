from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.metrics import dp
from kivy.app import App
import os
from model.crud_cliente import insert_cliente

Builder.load_file('view/cadastrocliente.kv') 

class CadastroCliente(Screen):
    def reset_form(self):
        self.ids['cpf'] = ""
        self.ids['rg'] = ""
        self.ids['nome'] = ""
        self.ids['telefone'] = ""
        self.ids['email'] = ""
        

    def aviso_cadastro(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Cliente Salvo Com Sucesso",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Cliente!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("OK",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def cadastro_cliente(self,cpfText,rgText,nomeText,telefoneText,emailText):
        app = App.get_running_app()
        app.cpf = cpfText
        app.rg = rgText
        app.nome = nomeText
        app.telefone = telefoneText
        app.email = emailText
        insert_cliente(app.cpf, app.rg, app.nome, app.telefone, app.email)
        popup = CadastroCliente()
        popup.aviso_cadastro()
        self.manager.get_screen('cadastrocliente').reset_form()

    
