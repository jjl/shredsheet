import wx
from shredsheet import Shredsheet

class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="Shredsheet", size=(800,600))
        self._init_statusbar()
        self._init_menu()
        self._init_shredsheet()
        self._init_layout()
        self.Show(True)

    def _init_statusbar(self):
        self.CreateStatusBar()

    def _init_menu(self):
        self._menus = {}
        self.menuBar = wx.MenuBar()
        self.SetMenuBar(self.menuBar)
        self._init_file_menu()

    def _init_file_menu(self):
        filem = self._menus['file'] = wx.Menu()
        exitm = self._menus['file/exit'] = filem.Append(wx.ID_EXIT, "E&xit", "Exit")
        self.Bind(wx.EVT_MENU, self.onMenuExit, exitm)
        self.menuBar.Append(filem, "&File")

    def _init_layout(self):
#        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
#        self.SetSizerAndFit(self.sizer1)
#        self.notebook = wx.Notebook(self,style=wx.NB_TOP)
#        self.new_sheet()
#        self.grid = wx.grid.Grid(self)
        pass
        

    def _init_shredsheet(self):
        self.ss = Shredsheet(self)

    def new_sheet(self):
        new = wx.Window(self.notebook)
        self.notebook.AddPage(new,"New Page")

    def onMenuExit(self,e):
        self.Close(True)
