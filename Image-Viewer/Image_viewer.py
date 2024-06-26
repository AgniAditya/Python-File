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

global bar
bar=Label(window,text="image 0 of "+str(len(image_list)-1),bd=1,relief=SUNKEN)
bar.grid(row=2,column=1,pady=10,sticky=W+E)

def forward(img_no):
    global lab
    global forward_button
    global backward_button
    global bar
    bar.grid_forget()
    lab.grid_forget() 
    lab1=Label(window,image=image_list[img_no],width=500,height=500)
    forward_button=Button(window,text=">>",command=lambda:forward(img_no+1))
    backward_button=Button(window,text="<<",command=lambda:backward(img_no-1))
    bar=Label(window,text="image "+str(img_no)+" of "+str(len(image_list)-1),bd=1,relief=SUNKEN)
    bar.grid(row=2,column=1,sticky=W+E,pady=10)
    if img_no==5:
        forward_button=Button(window,text=">>",state=DISABLED)
    backward_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)
    lab1.grid(row=0,column=0,columnspan=3)

def backward(img_no):
    global lab
    global forward_button
    global backward_button
    global bar
    bar.grid_forget()
    lab.grid_forget()
    lab=Label(window,image=image_list[img_no],width=500,height=500)
    forward_button=Button(window,text=">>",command=lambda:forward(img_no+1))
    backward_button=Button(window,text="<<",command=lambda:backward(img_no-1))
    bar=Label(window,text="image "+str(img_no)+" of "+str(len(image_list)-1),bd=1,relief=SUNKEN)
    bar.grid(row=2,column=1,sticky=W+E,pady=10)
    if img_no==0:
        backward_button=Button(window,text="<<",state=DISABLED)
    backward_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)
    lab.grid(row=0,column=0,columnspan=3)

backward_button=Button(window,text="<<",command=backward,state=DISABLED)
exit_button=Button(window,text="Exit",command=exit)
forward_button=Button(window,text=">>",command=lambda:forward(1))
forward_button.grid(row=1,column=2)
exit_button.grid(row=1,column=1)
backward_button.grid(row=1,column=0)


window.mainloop()