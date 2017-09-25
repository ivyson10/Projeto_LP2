from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, SlideTransition


class RootWidget4(BoxLayout, Screen):
    pass
class cadprodutoApp(App):
    def build(self):
        return RootWidget4()


def main():
    cadprodutoApp().run()

if __name__ == '__main__':
    main()    