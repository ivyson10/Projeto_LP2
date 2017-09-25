from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, SlideTransition


class RootWidget(BoxLayout, Screen):
    pass
class regfuncApp(App):
    def build(self):
        return RootWidget()


def main():
    regfuncApp().run()

if __name__ == '__main__':
    main()    