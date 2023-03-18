from tkinter import*
import speedtest
root=Tk()
root.title("INTERNET SPEED TEST")
root.geometry("540x1000")
root.resizable(False,False)
root.configure(bg="black")

def upinfo():
  info="Upload speed is the rate that online data is\n transferred from your computer to the Internet.\nThe upload speed is measured in\n Megabits per second (Mbps)."
  button2=Button(root,text=info,font="roboto 15 bold",bg="light blue",command=lambda:call(button2),bd=10)
  button2.pack(pady=10,ipady=10)
def downinfo():
  info="Download speed refers to the rate that digital data\n is transferred from the Internet to your computer.\nThe download speed is measured in\n Megabits per seconds (Mbps)."
  button2=Button(root,text=info,font="roboto 15 bold",bg="light blue",borderwidth=10,command=lambda:call(button2))
  button2.pack(pady=10,ipady=10)
def pinginfo():
  info="Ping means the time it takes for a small data set to\n be transmitted from your device to a server on\n the Internet and back to your device again.\n The ping time is measured in milliseconds" 
  button2=Button(root,text=info,font="roboto 15 bold",bg="light blue",borderwidth=10,command=lambda:call(button2))
  button2.pack(pady=10,ipady=10)
def call(Button):
  Button.pack_forget()
def check():
  test=speedtest.Speedtest()
  uploading=round(test.upload()/(1024*1024),2)
#upload.config(text=uploading)

  downloading=round(test.download()/(1024*1024),2)
#download.config(text=downloading)
# Download.config(text=downloading)
  servernames=[]
  test.get_servers(servernames)
  ping1=test.results.ping

  ping=Label(root,text=ping1,font="arial 28 bold",bg="black",fg="white")
  ping.place(x=115,y=70,anchor="center")
  download=Label(root,text=downloading,font="arial 28 bold",bg="black",fg="white")
  download.place(x=265,y=70,anchor="center")
  upload=Label(root,text=uploading,font="arial 28 bold",bg="black",fg="white")
  upload.place(x=415,y=70,anchor="center")
  Download=Label(root,text=downloading,font="arial 35 bold",bg="black",fg="white")
  Download.place(x=265,y=390,anchor="center")

image_icon=PhotoImage(file="D:\png image.png")
root.iconphoto(False,image_icon)
main=PhotoImage(file="D:\whole2.png")
Label(root,image=main,bg="black").pack()
button=Button(root,text="Start",font=("arial",25,"bold"),fg="black",bg="light blue",bd=12,activebackground="white",cursor="hand2",command=check)
button.pack(pady=(5,0))
b1=Button(root,text="PING",font="arial 10 bold",bg="light blue",bd=5,command=pinginfo).place(x=100,y=150)
b2=Button(root,text="DOWNLOAD",font="arial 10 bold",bg="light blue",bd=5,command=downinfo).place(x=228,y=150)
b3=Button(root,text="UPLOAD",font="arial 10 bold",bg="light blue",bd=5,command=upinfo).place(x=390,y=150)
Label(root,text="MS",font="arial 15 bold",bg="black",fg="blue").place(x=100,y=110)
Label(root,text="MBPS",font="arial 15 bold",bg="black",fg="blue").place(x=240,y=110)
Label(root,text="MBPS",font="arial 15 bold",bg="black",fg="blue").place(x=390,y=110)

Label(root,text="Download",font="arial 15 bold",bg="black",fg="blue").place(x=223,y=330)
Label(root,text="MBPS",font="arial 15 bold",bg="black",fg="blue").place(x=239,y=420)
root.mainloop()