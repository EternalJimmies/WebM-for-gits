import sys
from tkinter import *
import subprocess

def CreateWebms():
   print("The number of webms you wish to create is: %s" % (numin.get()))
   if (var.get() != 1):
      print(var.get())
      for i in range(int(numin.get())):
         print(vidin.get())
         print(vid[0].get())
         if (len(vid)>1):
            print(vid[1].get())
         subprocess.call('ffmpeg -i %s -ss %s -to %s -c:v libvpx -crf 4 -b:v %sK -vf scale=%s:%s %s.webm' % (vid[0].get(), start[0].get(), end[0].get(), bitrate[0].get(), width[0].get(), height[0].get(), out[0].get()), shell=True)
         print("Conversion done")
   else:
      print(var.get())
      subprocess.call('ffmpeg -i %s -ss %s -to %s -c:v libvpx -crf 4 -b:v %sK -vf scale=%s:%s %s.webm' % (vid[0].get(), start[0].get(), end[0].get(), bitrate[0].get(), width[0].get(), height[0].get(), out[0].get()), shell=True)
   ClearFields()
   
def ClearFields():
   for field in fields:
      field.delete(0,END)

def AdvancedOptions():
   if (var.get() != 0):
      crf.grid(row=8, column=1)
      thr.grid(row=9, column=1)
   else:
      crf.grid_remove()
      thr.grid_remove()

master = Tk()

vid = []
start = []
end = []
bitrate = []
width = []
height = []
out = []

Label(master, text="Number of webms").grid(row=0)
Label(master, text="Filename").grid(row=1)
Label(master, text="Start time").grid(row=2)
Label(master, text="End time").grid(row=3)
Label(master, text="Bitrate").grid(row=4)
Label(master, text="Width").grid(row=5)
Label(master, text="Height").grid(row=6)
Label(master, text="Output Filename").grid(row=7)
Label(master, text="crf").grid(row=8)
Label(master, text="Amounts of threads").grid(row=9)

numin = Entry(master)
vidin = Entry(master)
vid.append(vidin)
startin = Entry(master)
start.append(startin)
endin = Entry(master)
end.append(endin)
bitratein = Entry(master)
bitrate.append(bitratein)
widthin = Entry(master)
width.append(widthin)
heightin = Entry(master)
height.append(heightin)
outin = Entry(master)
out.append(outin)
crf = Entry(master)
thr = Entry(master)

numin.grid(row=0, column=1)
vidin.grid(row=1, column=1)
startin.grid(row=2, column=1)
endin.grid(row=3, column=1)
bitratein.grid(row=4, column=1)
widthin.grid(row=5, column=1)
heightin.grid(row=6, column=1)
outin.grid(row=7, column=1)

fields = [vidin, startin, endin, bitratein, widthin, heightin, outin, crf, thr]

Button(master, text='Enter', command=CreateWebms).grid(row=10, column=1, sticky=W, pady=4)
var = IntVar()
Checkbutton(master, text = "Advanced Options", command=AdvancedOptions, variable = var ,height=5, width = 20).grid(row=10)

mainloop()

