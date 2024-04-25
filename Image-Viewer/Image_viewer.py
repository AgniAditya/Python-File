from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title("Image Viewer")
window.iconbitmap("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/Image-Viewer/multimediaphotoviewer_94421.ico")

img_1=ImageTk.PhotoImage(Image.open("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/Image-Viewer/aidtya-01.jpg"))
img_2=ImageTk.PhotoImage(Image.open("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/Image-Viewer/space-01.jpg"))
img_3=ImageTk.PhotoImage(Image.open("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/Image-Viewer/space-02.jpeg"))
img_4=ImageTk.PhotoImage(Image.open("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/Image-Viewer/space-03.jpeg"))
img_5=ImageTk.PhotoImage(Image.open("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/Image-Viewer/space-04.jpeg"))
img_6=ImageTk.PhotoImage(Image.open("C:/Users/agnih/OneDrive/Desktop/python/Tkinter/Image-Viewer/space-05.jpeg"))

global image_list
image_list=[img_1,img_2,img_3,img_4,img_5,img_6]

lab=Label(image=img_1,width=500,height=500)
lab.grid(columnspan=3)

def forward(img_no):
    global lab
    global forward_button
    global backward_button
    lab.grid_forget()
    forward_button.grid_forget()
    # for i in image_list:
    lab1=Label(window,image=image_list[img_no-1],width=500,height=500)
    forward_button=Button(window,text=">>",command=lambda:forward(img_no+1))
    if img_no==5:
        forward_button=Button(window,text=">>",state=DISABLED)
    forward_button.grid(row=1,column=2)
    lab1.grid(row=0,column=0,columnspan=3)

def backward(img_no):
    global lab
    global forward_button
    global backward_button
    lab.grid_forget()
    backward_button.grid_forget()
    lab1=Label(window,image=image_list[img_no+1],width=500,height=500)
    backward_button=Button(window,text="<<",command=lambda:backward(img_no-1))
    if img_no==5:
        backward_button=Button(window,text="<<",state=DISABLED)
    backward_button.grid(row=1,column=0)
    lab1.grid(row=0,column=0,columnspan=3)

backward_button=Button(window,text="<<",command=lambda:backward(0))
exit_button=Button(window,text="Exit",command=exit)
forward_button=Button(window,text=">>",command=lambda:forward(2))
forward_button.grid(row=1,column=2)
exit_button.grid(row=1,column=1)
backward_button.grid(row=1,column=0)

window.mainloop()