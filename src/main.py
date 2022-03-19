from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

from kivy.core.window import Window
from kivy.lang import Builder

from re import compile as re_compile

main_kv = '''
ScreenManager:
    Login
    Cadastro
    Recuperacao
    Navegacao
'''

Builder.load_file('layout/login.kv')
Builder.load_file('layout/cadastro.kv')
Builder.load_file('layout/recuperacao.kv')
Builder.load_file('layout/navegacao.kv')


email_pattern = re_compile('^[a-z][a-z0-9.]+@[a-z][a-z0-9.]+$')
number_pattern = re_compile('^[0-9]+ [0-9-]+$')

class DoeAgora(MDApp):
    def build(self):
        self.previous_screens = []

        return Builder.load_string(main_kv)
    
    def enter_screen(self, name: str):
        self.previous_screens.append(self.root.current)
        self.root.transition.direction = 'left'
        self.root.current = name
    
    def leave_screen(self):
        self.root.transition.direction = 'right'
        self.root.current = self.previous_screens.pop()
    
    def check_email_or_number (self, textfield: MDTextField):
        textfield.error = not bool(email_pattern.match(textfield.text) or number_pattern.match(textfield.text))


if __name__ == '__main__':
    Window.size = (300, 600)

    DoeAgora().run()