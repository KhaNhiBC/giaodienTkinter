from tkinter import *
root = Tk()
root.title("hello")
Label(root,
      text = "Hello ! I'm Tkinter",
      justify=CENTER,relief=SUNKEN).pack(pady = 10)
photo = PhotoImage(file ="hinh3.png")
Label (root, image = photo, relief = RAISED).pack(side = LEFT,padx = 5)

Label(root,text="Do you want to quit ?").pack(pady = 50,padx = 10)
Button(root,text = "NO").pack(side=RIGHT)
Button(root,text="YES",command=root.quit).pack(side=RIGHT)

Label(root, text="Enter your name:").pack(side=BOTTOM, padx = 10,pady = 10)
e = StringVar()
Entry(root,width = 40, textvariable = e).pack(side=BOTTOM)
#e.set("")
Button(root,text="OK").pack(side=BOTTOM)

root.resizable(height = True, width = True)
root.minsize(height = 360, width = 360)

def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth()//2) - (width//2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
makecenter(root)



root.mainloop()

