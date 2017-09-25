from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from regcliente import RootWidget
from venda import RootWidget2
from cadproduto import RootWidget4

class RootWidget1(BoxLayout, Screen):
    def tlCadCliente(self):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = 'regcliente'
    def CadVenda(self):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = 'venda'
    def CadProduto(self):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = 'cadproduto'
class MenuApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(RootWidget(name='regcliente')) 
        manager.add_widget(RootWidget2(name='venda'))
        manager.add_widget(RootWidget4(name='cadproduto'))   
        return manager
   


 


def main():
    MenuApp().run()

if __name__ == '__main__':
    main()    