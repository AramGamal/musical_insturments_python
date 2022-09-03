
from turtle import bgcolor, color
from playsound import playsound
import tkinter
from tkinter import*
import threading
import winsound
import sys
import os

#initializing our gui

top = Tk()
top.title("musical insturments")
top.minsize(800,500)





label_menu = Label(top,bg="black")
label_menu.place(x=0,y=0,relwidth=1,relheight=1)
label2_menu = Label(text="Musical Insturments",font=("helvetica",40),fg="white",bg="black")
label2_menu.place(relx=0.5,rely=0.4, anchor=CENTER)
label3_menu = Label(text="choose the insturment from the menu bar",font=("helvetica",20),fg="white",bg="black")
label3_menu.place(relx=0.5,rely=0.5, anchor=CENTER)




def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




def do():
    playsound(resource_path('piano_tones/do.mp3'),block=False)
    # label.configure(bg='#000000')
    # label2.configure(bg='#000000')
   

def re():
    playsound(resource_path('piano_tones/re.mp3'),block=False)
    # label.configure(bg='#0d0d0d')
    # label2.configure(bg='#0d0d0d')

def me():
    playsound(resource_path('piano_tones/me.mp3'),block=False)    
    # label.configure(bg='#1a1a1a')
    # label2.configure(bg='#1a1a1a')

def fa():
    playsound(resource_path('piano_tones/fa.mp3'),block=False)
    # label.configure(bg='#262626')
    # label2.configure(bg='#262626')

def sol():
    playsound(resource_path('piano_tones/sol.mp3'),block=False)
    # label.configure(bg='#333333')
    # label2.configure(bg='#333333')


def la():
    playsound(resource_path('piano_tones/la.mp3'),block=False)
    # label.configure(bg='#404040')
    # label2.configure(bg='#404040')

def si():
    playsound(resource_path('piano_tones/si.mp3'),block=False)
    # label.configure(bg='#4d4d4d')
    # label2.configure(bg='#4d4d4d')

def do_sharp():
    playsound(resource_path('piano_tones/do_sharp.mp3'),block=False)
    # label.configure(bg='#595959')
    # label2.configure(bg='#595959')

##piano functions









#drums functions

def kick():
    playsound('drums_tones/kick.mp3',block=False)
    # label.configure(bg='#000000')
    # label2.configure(bg='#000000')
   

def hihat():
    playsound('drums_tones/hihat.mp3',block=False)
    # label.configure(bg='#0d0d0d')
    # label2.configure(bg='#0d0d0d')

def snare():
    playsound('drums_tones/snare.mp3',block=False)    
    # label.configure(bg='#1a1a1a')
    # label2.configure(bg='#1a1a1a')

def kick_hihat():
    playsound('drums_tones/kick+hihat.mp3',block=False)
    # label.configure(bg='#262626')
    # label2.configure(bg='#262626')

def crash():
    playsound('drums_tones/crash.mp3',block=False)
    # label.configure(bg='#333333')
    # label2.configure(bg='#333333')


def hitom():
    playsound('drums_tones/hitom.mp3',block=False)
    # label.configure(bg='#404040')
    # label2.configure(bg='#404040')

def midtom():
    playsound('drums_tones/midtom.mp3',block=False)
    # label.configure(bg='#4d4d4d')
    # label2.configure(bg='#4d4d4d')

def lotom():
    playsound('drums_tones/lotom.mp3',block=False)
    # label.configure(bg='#595959')
    # label2.configure(bg='#595959')

def snr_crsh():
    playsound('drums_tones/snr+crsh.mp3',block=False)
    # label.configure(bg='#595959')
    # label2.configure(bg='#595959')

def ride():
    playsound('drums_tones/ride.mp3',block=False)
    # label.configure(bg='#595959')
    # label2.configure(bg='#595959')

##drums functions









def drums():
    #background

    labeld = Label(top,bg="black")
    labeld.place(x=0,y=0,relwidth=1,relheight=1)

    label2d = Label(text="Drum rolls!",font=("Segoe Script",40),fg="white",bg="black")
    label2d.place(relx=0.5,rely=0.15, anchor=CENTER)
    btn1d = Button(text='kick',height=10,width=10,command=kick)
    btn1d.pack()
    btn1d.place(relwidth=0.1,relheight=0.1,relx=0.005,rely=0.400)

    btn2d = Button(text='hihat',height=10,width=10,command=hihat)
    btn2d.pack()
    btn2d.place(relwidth=0.1,relheight=0.1,relx=0.105,rely=0.500)

    btn3d = Button(text='snare',height=10,width=10,command=snare)
    btn3d.pack()
    btn3d.place(relwidth=0.1,relheight=0.1,relx=0.205,rely=0.400)

    btn4d = Button(text='Kick+HiHat',height=10,width=10,command=kick_hihat)
    btn4d.pack()
    btn4d.place(relwidth=0.1,relheight=0.1,relx=0.305,rely=0.500)

    btn5d = Button(text='crash',height=10,width=10,command=crash)
    btn5d.pack()
    btn5d.place(relwidth=0.1,relheight=0.1,relx=0.405,rely=0.400)

    btn6d = Button(text='hitom',height=10,width=10,command=hitom)
    btn6d.pack()
    btn6d.place(relwidth=0.1,relheight=0.1,relx=0.505,rely=0.500)

    btn7d = Button(text='midtom',height=10,width=10,command=midtom)
    btn7d.pack()
    btn7d.place(relwidth=0.1,relheight=0.1,relx=0.605,rely=0.400)

    btn8d = Button(text='lotom',height=10,width=10,command=lotom)
    btn8d.pack()
    btn8d.place(relwidth=0.1,relheight=0.1,relx=0.705,rely=0.500)

    btn9d = Button(text='snr+crsh',height=10,width=10,command=snr_crsh)
    btn9d.pack()
    btn9d.place(relwidth=0.1,relheight=0.1,relx=0.805,rely=0.400)

    btn10d = Button(text='ride',height=10,width=10,command=ride)
    btn10d.pack()
    btn10d.place(relwidth=0.1,relheight=0.1,relx=0.905,rely=0.500)






    top.bind('1', lambda event:threading.Thread(target=kick).start())
    top.bind('2', lambda event:threading.Thread(target=hihat).start())
    top.bind('3', lambda event:threading.Thread(target=snare).start())
    top.bind('4', lambda event:threading.Thread(target=kick_hihat).start())
    top.bind('5', lambda event:threading.Thread(target=crash).start())
    top.bind('6', lambda event:threading.Thread(target=hitom).start())
    top.bind('7', lambda event:threading.Thread(target=midtom).start())
    top.bind('8', lambda event:threading.Thread(target=lotom).start())
    top.bind('9', lambda event:threading.Thread(target=snr_crsh).start())
    top.bind('0', lambda event:threading.Thread(target=ride).start())









def piano():
    #background

    label = Label(top,bg="black")
    label.place(x=0,y=0,relwidth=1,relheight=1)

    label2 = Label(text="start playing!",font=("Segoe Script",40),fg="white",bg="black")
    label2.place(relx=0.5,rely=0.15, anchor=CENTER)
    btn1 = Button(text='do',height=10,width=10,command=do)
    btn1.pack()
    btn1.place(relwidth=0.1,relheight=0.3,relx=0.02,rely=0.400)

    btn2 = Button(text='re',height=10,width=10,command=re)
    btn2.pack()
    btn2.place(relwidth=0.1,relheight=0.3,relx=0.14,rely=0.400)

    btn3 = Button(text='me',height=10,width=10,command=me)
    btn3.pack()
    btn3.place(relwidth=0.1,relheight=0.3,relx=0.26,rely=0.400)

    btn4 = Button(text='fa',height=10,width=10,command=fa)
    btn4.pack()
    btn4.place(relwidth=0.1,relheight=0.3,relx=0.38,rely=0.400)

    btn5 = Button(text='sol',height=10,width=10,command=sol)
    btn5.pack()
    btn5.place(relwidth=0.1,relheight=0.3,relx=0.5,rely=0.400)

    btn6 = Button(text='la',height=10,width=10,command=la)
    btn6.pack()
    btn6.place(relwidth=0.1,relheight=0.3,relx=0.62,rely=0.400)

    btn7 = Button(text='si',height=10,width=10,command=si)
    btn7.pack()
    btn7.place(relwidth=0.1,relheight=0.3,relx=0.74,rely=0.400)

    btn8 = Button(text='do',height=10,width=10,command=do_sharp)
    btn8.pack()
    btn8.place(relwidth=0.1,relheight=0.3,relx=0.86,rely=0.400)






    top.bind('1', lambda event:threading.Thread(target=do).start())
    top.bind('2', lambda event:threading.Thread(target=re).start())
    top.bind('3', lambda event:threading.Thread(target=me).start())
    top.bind('4', lambda event:threading.Thread(target=fa).start())
    top.bind('5', lambda event:threading.Thread(target=sol).start())
    top.bind('6', lambda event:threading.Thread(target=la).start())
    top.bind('7', lambda event:threading.Thread(target=si).start())
    top.bind('8', lambda event:threading.Thread(target=do_sharp).start())













##piano functions





#adding a menu bar
menu = Menu(top)
top.config(menu=menu)

insturment_menu = Menu(menu)
exit_menu = Menu(menu)
menu.add_cascade(label='insturment',menu=insturment_menu)
insturment_menu.add_command(label='piano',command=piano)
insturment_menu.add_command(label='drums',command=drums)
menu.add_cascade(label='exit',menu=exit_menu)
exit_menu.add_cascade(label="exit",command=top.quit)


top.mainloop()







