from Tkinter import *

width=10
height=10
grid = []

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def columnName(idx):
    assert(idx != 0)
    ret = []
    alpha = lambda x: ALPHABET[x-1]
    while (idx > 26):
        div = idx / 26
        ret.append(alpha(div))
        idx -= (div*26) # Save modulus
    ret.append(alpha(idx))
    return "".join(ret)

root = Tk()

frame = Frame(root, width=500, height=300)

row1 = []

for x in range(1,10):
    row1.append(Label(frame,text=columnName(x)))

for y in range(1,10):
    grid.append([Entry(frame) for y in range(2,10)])


