from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.app import App
from model.crud_vendedor import insert_vendedor

Builder.load_file('view/cadastrovendedor.kv') 

class CadastroVendedor(Screen):
    def aviso_cadastro(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Vendedor Salvo Com Sucesso",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Vendedor!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("OK",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
    def cadastro_vendedor(self,cpfText,rgText,nomeText,telefoneText,emailText,senhaText):
        app = App.get_running_app()
        app.cpf = cpfText
        app.rg = rgText
        app.nome = nomeText
        app.telefone = telefoneText
        app.email = emailText
        app.senha = senhaText
        insert_vendedor(app.cpf, app.rg, app.nome, app.telefone, app.email, app.senha)
        popup = CadastroVendedor()
        popup.aviso_cadastro()