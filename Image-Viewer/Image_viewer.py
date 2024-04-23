from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title("Image Viewer")
window.iconbitmap("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/multimediaphotoviewer_94421.ico")

img_1=ImageTk.PhotoImage(Image.open("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/aidtya-01.jpg"))
lab=Label(image=img_1,width=1118,height=800)
lab.pack()

exit_button=Button(window,text="Exit",command=exit)
exit_button.pack()

window.mainloop()