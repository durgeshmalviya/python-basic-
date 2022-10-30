from tkinter import *
from turtle import down
import speedtest

root=Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(bg="#000000")

def Check():
    test=speedtest.Speedtest()
    
    Uploading=round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)
    
    downloading=round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)
    
    servernames= []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)
    
    
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="top.png")
Label(root,image=Top,bg="#000000").pack()

Main=PhotoImage(file="main.png")
Label(root,image=Main,bg="#000000").pack(pady=(40,0))

button=PhotoImage(file="button.png")
Button=Button(root,image=button,bg="#000000",bd=0,activebackground="#000000",cursor="hand2",command=Check)
Button.pack(pady=10)

Label(root,text="Ping",font="arial 10 bold",bg="#A9A9A9").place(x=50,y=0)
Label(root,text="Download",font="arial 10 bold",bg="#A9A9A9").place(x=150,y=0)
Label(root,text="Upload",font="arial 10 bold",bg="#A9A9A9").place(x=260,y=0)

Label(root,text="Ms",font="arial 10 bold",bg="#000000",fg="#A9A9A9").place(x=60,y=80)
Label(root,text="Mbps",font="arial 10 bold",bg="#000000",fg="#A9A9A9").place(x=160,y=80)
Label(root,text="Mbps",font="arial 10 bold",bg="#000000",fg="#A9A9A9").place(x=275,y=80)

Label(root,text="Download",font="arial 15 bold",bg="#000000",fg="#A9A9A9").place(x=140,y=280)
Label(root,text="Mbps",font="arial 10 bold",bg="#000000",fg="#A9A9A9").place(x=165,y=380)

ping=Label(root,text="00",font="arial 10 bold",bg="#000000",fg="#A9A9A9")
ping.place(x=70,y=60,anchor="center")

download=Label(root,text="00",font="arial 10 bold",bg="#000000",fg="#A9A9A9")
download.place(x=180,y=60,anchor="center")

upload=Label(root,text="00",font="arial 10 bold",bg="#000000",fg="#A9A9A9")
upload.place(x=290,y=60,anchor="center")

Download=Label(root,text="00",font="arial 30 bold",bg="#A9A9A9")
Download.place(x=185,y=350,anchor="center")

root.mainloop()