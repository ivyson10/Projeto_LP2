from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.app import App
import view.meu
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.metrics import dp
from model.crud_vendedor import valida_senha

Builder.load_file('view/login.kv') 

class Login(Screen):
    def aviso(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Usuário ou senha estão errados",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Atenção!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("OK",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def entrar(self, loginText, SenhaText):
        app = App.get_running_app()
        app.login = loginText
        app.senha = SenhaText
        if valida_senha(app.login, app.senha):
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'principal'
        else:
            popup = Login()
            popup.aviso()
        
