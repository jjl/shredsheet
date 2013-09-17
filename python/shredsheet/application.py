import wx
from mainwindow import MainWindow

class Application(wx.App):
    
    def __init__(self,do_redir=False):
        """
        do_redir: redirect stdout, stderr to a window
        """
        wx.App.__init__(self,do_redir)
        self.mw = MainWindow()
         
    def run(self):
        self.MainLoop()
        


        
