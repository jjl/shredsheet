import wx.grid

class Grid(wx.grid.GridTableBase):
    
    def __init__(self):
        wx.grid.GridTableBase.__init__(self)

    def GetNumberRows(self):
        return 1

    def GetNumberCols(self):
        return 1

    def IsEmptyCell(self):
        return False
