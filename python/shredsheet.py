import Tkinter as Tk

class Shredsheet(Tk.Frame):

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sheetWidth=10
    sheetHeight=10

    def __init__(self,master=None):
        Tk.Frame.__init__(self,master,width=500,height=300)
        self._init_sheet()
        self.grid()

    def _init_sheet(self):
        self.cells = [self._makeTitleRow(self.sheetWidth)]
        for r in range(1,(self.sheetHeight+1)):
            row = self._makeRow(r,self.sheetWidth)
            self.cells.append(row)

    def _makeTitleRow(self, length):
        row = [None]
        for i in range(1,(length+1)):
            row.append(self._columnLabel(i))
        return row
        
    def _makeRow(self, rowIndex,length):
        row = [self._rowLabel(rowIndex)]
        for c in range(1,(length+1)):
            row.append(self._gridEntry(c,rowIndex))
        return row
        
    def _alphaIndex(self,idx):
        return self.ALPHABET[idx-1]

    def _columnName(self,idx):
        assert(idx != 0)
        ret = []
        while (idx > 26):
            (idx,rmdr) = divmod(idx,26)
            ret.append()
            ret.append(self._alphaIndex(rmdr))
        ret.append(self._alphaIndex(idx))
        ret.reverse()
        return "".join(ret)

    def _columnLabel(self,colIndex):
        l = Tk.Label(self, text=self._columnName(colIndex))
        l.grid(row=0,column=colIndex)
        return l

    def _rowLabel(self,rowIndex):
        l = Tk.Label(self,text=rowIndex)
        l.grid(row=rowIndex,column=0)
        return l

    def _gridEntry(self,x,y):
        e = Tk.Entry(self,width=5)
        e.grid(row=y,column=x)
        return e

if __name__ == '__main__':
    s = Shredsheet()
    s.mainloop()
