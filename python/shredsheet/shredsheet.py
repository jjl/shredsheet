import wx
import wx.grid
from util.numbase import Numbase

class Shredsheet(wx.grid.Grid):

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sheetWidth=50
    sheetHeight=50

    def __init__(self,parent,width=None,height=None):
        wx.grid.Grid.__init__(self,parent)
        # self does not exist at default param time
        if width is None: width = self.sheetWidth
        if height is None: height = self.sheetHeight
        self.CreateGrid(width,height)
        self.numbase = Numbase(self.ALPHABET)

    def columnNameToNumber(self,name):
        return self.numbase.numeric(name)

    def columnNumberToName(self,num):
        return self.numbase.written(num)
