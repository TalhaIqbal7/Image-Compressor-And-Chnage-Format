# Import Module
# import tkinter as tk
# from tkinter import ttk,filedialog
# from tkinter.filedialog import askopenfile
# import os
# import sys
# from PIL import Image
# # create root window
# root = tk.Tk()

# # root window title and dimension
# root.title("Image Compressor")
# # Set geometry(widthxheight)
# root.geometry('1000x600+400+250')
# #MAIN FUNCTION
# #def Destroy():
# #root.tk.destroy
# root['background']='#23272a'
# #adding a label to the root window
# # Create a Button

# # Add a Label widget
# label = tk.Label(root, text="Select the images ", font=('Georgia 13'))
# label.pack(pady=10)

# # Create a Button
# def change_format():
#     verbose = False
#     if (len(sys.argv)>1):
        
#         if (sys.argv[1].lower()=="-v"):
#             verbose = True
#     cwd = os.getcwd()

#     for filename in os.listdir(cwd): 
#         prefix = filename.split(".jpg")[0]
#         im = Image.open(filename)
#         strres=prefix+".png"
#         im.save(strres)
#     return
# #txt.grid(column =1, row =0)
# #btn = ttk.Button(root, text = 'Click me !', command = Destroy)
# def compressMe(file, verbose = False):
#     filepath = os.path.join(os.getcwd(), 
#                             file)
      
#     picture = Image.open(filepath)
#     picture.save("Compressed_"+file, 
#                  "JPEG", 
#                  optimize = True, 
#                  quality = 30)
#     return
# def main():
#     verbose = False
#     if (len(sys.argv)>1):
        
#         if (sys.argv[1].lower()=="-v"):
#             verbose = True
#     cwd = os.getcwd()
  
#     formats = ('.jpg', '.jpeg')
#     for file in os.listdir(cwd):
#         if os.path.splitext(file)[1].lower() in formats:
#             print('compressing', file)
#             compressMe(file, verbose)
#     print("Done")
# menu= tk.StringVar()
# menu.set("Select format")
# #Create a dropdown Menu
# drop="JPEG"
# drop= tk.OptionMenu(root, menu,".jpeg", ".jpg",".webp",".png")
# print(menu)
# #change_format()
# drop.pack()
# ttk.Button(root, text="Compress", command=main).pack(pady=20)
# # Set the position of button on the top of window.  
# #btn.pack(side = 'top')
# # Execute Tkinter
# root.mainloop()
#how to create simple GUI registration form.
#importing tkinter module for GUI application
from tkinter import *
import sys
import os
from PIL import Image
def change_format(sv):
    #print("IN CHANGE FORMAT")
    #print (dropd)
    print(drop_quality)
    verbose = False
    if (len(sys.argv)>1):
        if (sys.argv[1].lower()=="-v"):
            verbose = True
    cwd = os.getcwd()
    for filename in os.listdir(cwd): 
        if filename.endswith(".jpg"):
            prefix = filename.split(".")[0]
            im = Image.open(filename)
            strres=prefix+dropd
            im.save("Compressed_"+strres,optimize = True, quality=int(drop_quality))
    return
def compressMe(file, verbose = False):
    #print(drop_quality)
    filepath = os.path.join(os.getcwd(), file)
    picture = Image.open(filepath)
    picture.save("Compressed_"+file,optimize = True, quality=25)
    return
def _get(cur):
    global dropd
    dropd = cur
    return
def _get2(cur):
    global drop_quality
    drop_quality = cur
    return
def main():
    #print("IN MAIN")
    #print(dropd)
    verbose = False
    if (len(sys.argv)>1):
        
        if (sys.argv[1].lower()=="-v"):
            verbose = True
    cwd = os.getcwd()
    formats = ('.py')
    for file in os.listdir(cwd):
        if  os.path.splitext(file)[1].lower() not in formats:
            #print('compressing', file)
            #print(" ")
            change_format(file)
            #compressMe(file, verbose)
    #print("Done")
    root.quit()
#Creating object 'root' of Tk()
root = Tk()
#Providing Geometry to the form
root.geometry("500x500")
root['background']='#23272a'
#Providing title to the form
root.title('Registration form')
root.wm_attributes("-transparentcolor", 'grey')
#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Compress Images", bg='#23272a', fg='#fff', width=15,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)
#this creates list of countries available in the dropdownlist.
list_of_formats=[ '.WEBP' ,'.JPEG' , '.PNG' ,'.JPG']
#the variable 'c' mentioned here holds String Value, by default ""
sv = ".WEBP"          #<-- setting sv to default item
c=StringVar()
droplist=OptionMenu(root,c, command = _get,*list_of_formats)
droplist.config(width=10,bg='#23272a', fg='#fff')
#print (c)
#c.set(list_of_formats[0])     #<-- Setting default item to servs's first item
droplist.place(x=240,y=140)
##this creates 'Label' widget for Language and uses place() method.
label_6=Label(root,text="Format",width=20,font=('bold',10),bg='#23272a', fg='#fff')
label_6.place(x=75,y=140)

#FOR QUALITY
list_of_quality=[ '100' ,'75' , '50' ,'25','0']
#the variable 'c' mentioned here holds String Value, by default ""
d=StringVar()
droplist=OptionMenu(root,d, command = _get2,*list_of_quality)
droplist.config(width=10,bg='#23272a', fg='#fff')
#print (c)
#c.set(list_of_formats[0])     #<-- Setting default item to servs's first item
droplist.place(x=240,y=180)
##this creates 'Label' widget for Language and uses place() method.
label_6=Label(root,text="Quality",width=20,font=('bold',10),bg='#23272a', fg='#fff')
label_6.place(x=75,y=180)



#this creates button for submitting the details provides by the user
Button(root, text='Compress' , width=20,bg="#7A2F8F",fg='white',command=main).place(x=180,y=380)
#this will run the mainloop.
root.mainloop()
