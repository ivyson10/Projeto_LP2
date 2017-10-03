from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.metrics import dp

Builder.load_file('cadastrocliente.kv') 

class CadastroCliente(Screen):
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
