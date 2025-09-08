from kivy.app import App

class PytoriApp(App):
    def __init__(self, **kwargs):
        super(PytoriApp, self).__init__(**kwargs)
        self.title = 'pytori'

if __name__ == '__main__':
	PytoriApp().run()
