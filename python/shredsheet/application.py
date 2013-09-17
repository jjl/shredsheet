import Tkinter as Tk
from shredsheet import Shredsheet

class Application(Tk.Tk):
    
    def __init__(self):
        Tk.Tk.__init__(self)
        self._grid = Shredsheet(self)
        self.grid()
        
    def run(self):
        self.mainloop()
        


        
