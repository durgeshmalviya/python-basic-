from distutils import command
from imp import reload
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
class Grid_LayoutApp(App):
    def build(self,):  
             
        layout = GridLayout(cols = 20)
                
        App(Button,text ="Hello world ", command = quit)
        App(pady=50)
        
class MyLabelApp(App):
    	def build(self):
         return Label(text ="[Hello]",
         font_size ='40sp', markup = True)
App(pady=50)
        
        


root = Grid_LayoutApp()
root.run()
()
