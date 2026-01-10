from tkinter import*

root=Tk()

canvass=Canvas(root,width=400,height=300,bg='green')
canvass.create_line(0,0,40,48)
canvass.pack()

root.mainloop()

