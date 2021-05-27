from kivy.app import App				# importing kivy module

from kivy.uix.boxlayout import BoxLayout		# Arrange in horizontal or vertical blocks
from kivy.uix.gridlayout import GridLayout		# arranges in grid like structure e.g when col=3 we have 3x3 matrix

from kivy.uix.button import Button			# kivy built in button function	
from kivy.config import Config				# for configuration window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Config.set("graphics","resizable","1")
Config.set("graphics","width","500")
Config.set("graphics","height","500")

choice = ['X', 'O']; switch = 0				# semi colon is used to put multiple statements in one line

class MainApp(App):

    def tic_tac_toe(self, arg):		
        global switch			# global is function used inside functions to make local variables global

        arg.disabled = True		
        arg.text = choice[switch]

        if not switch: switch = 1
        else: switch = 0

        coordinate = (
            (0,1,2),(3,4,5),(6,7,8), # X
            (0,3,6),(1,4,7),(2,5,8), # Y
            (0,4,8),(2,4,6),         # D
        )

        vector = (
            [self.button[x].text for x in (0,1,2)],
            [self.button[x].text for x in (3,4,5)],
            [self.button[x].text for x in (6,7,8)],

            [self.button[y].text for y in (0,3,6)],
            [self.button[y].text for y in (1,4,7)],
            [self.button[y].text for y in (2,5,8)],

            [self.button[d].text for d in (0,4,8)],
            [self.button[d].text for d in (2,4,6)],
        )

        win = False
        color = [0,1,0,1] # Green

        for index in range(8):
            if vector[index].count('X') == 3\
            or vector[index].count('O') == 3: 
                win = True
                for i in coordinate[index]:
                    self.button[i].color = color
		
                break

        if win:
            for index in range(9):
                self.button[index].disabled = True
            
            


           
    def restart(self, arg):
        global switch; switch = 0
        for index in range(9):
            self.button[index].color = [0,0,0,1]
            self.button[index].text = ""
            self.button[index].disabled = False
    def clk(self, obj):
        popup = Popup(title="GROUP 5",
              content=Label(text='MADE BY:\n\nKAMRAN SAIF',font_size='25sp'),
              size_hint=(.8, .8))
        popup.open()
    def build(self):
        self.title = "Tic Tak Tok by Group 5"
        
        root = BoxLayout(orientation = "vertical", padding = 5)

        grid = GridLayout(cols = 3)
        self.button = [0 for _ in range(9)]
        for index in range(9):
            self.button[index] = Button(
                    color = [0,0,0,1],
                    font_size = 60,
                    disabled = False,
                    on_press = self.tic_tac_toe
                )
            grid.add_widget(self.button[index])
        root.add_widget(grid)

        root.add_widget(
            Button(
		text="Credit : GROUP 5",font_size='30sp',
            	size_hint = [1,.1],
            	on_press = self.clk

            )
        )
        root.add_widget(
            Button(
                text = "Restart",font_size='30sp',
                size_hint = [1,.1],
                on_press = self.restart
            )
	)
	
        return root

if __name__ == "__main__":
    MainApp().run()
