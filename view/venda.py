from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, SlideTransition


class RootWidget2(BoxLayout, Screen):
    pass
class VendaApp(App):
    def build(self):
        return RootWidget2()


def main():
    VendaApp().run()

if __name__ == '__main__':
    main()    