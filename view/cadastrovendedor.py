from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 


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