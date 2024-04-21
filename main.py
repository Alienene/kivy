from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

class MyApp(App):
    def build(self):
        button = Button(text='натисни')
        self.label = Label(text='привіт')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(button)
        layout.add_widget(self.label)
        button.bind(on_press=self.click_button)
        return layout

    def click_button(self,instance):
        list1 = []
        a = ''
        for _ in range(8):
            #list1.append(random.randint(1, 10))
            a += str(random.randint(1,10))
        self.label.text = (a)

if __name__ == '__main__':
    MyApp().run()
