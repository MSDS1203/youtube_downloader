import tkinter as tk
from tkinter import *
import yt_dlp
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

#set the icon
import ctypes 
myapp='mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp)


root = tk.Tk()
root.geometry('800x300')
root.resizable(False,False)

root.title('Youtube Downloader')
root.config(background='#88d3db')

img = Image.open('camera_reel.webp')
img = ImageTk.PhotoImage(img)
root.iconphoto(False,img)

link = StringVar()
download_path = StringVar()

def functionality():
    title_label = Label(root, text = 'Youtube Video Downloader', padx=10, pady=15, font="Times 14", bg="#7ca1ff", fg='black')
    title_label.grid(row=1,column=1,padx=15,pady=15,columnspan=3)
    link_label = Label(root, text="Youtube URl: ", bg="#7874ed")
    link_label.grid(row=2,column=0, padx=15, pady=15)

    root.linktext = Entry(root, width=40, textvariable=link, font="Times 14")
    root.linktext.grid(row=2,column=1,padx=15,pady=15,columnspan=3)

def Location():
    directory = filedialog.askdirectory(initialdir="PATH", title='Save Video')
    download_path.set(directory)

def Download_Video():
    YouTube_link = link.get().strip()
    download_folder = download_path.get()

    if not YouTube_link.startswith("http"):
        messagebox.showerror("Invalid URL", "Please enter a valid YouTube link.")
        return

    ydl_opts = {
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([YouTube_link])
        messagebox.showinfo("Success", f"Video downloaded to:\n{download_folder}")
    except Exception as e:
        messagebox.showerror("Download Failed", f"An error occurred:\n{e}")

destination_label = Label(root, text="Selected Path: ", bg="#a291c7")
destination_label.grid(row=3,column=0,padx=15,pady=15)

root.destinationtext = Entry(root, width=40, textvariable=download_path, font="Times 14")
root.destinationtext.grid(row=3,column=1,padx=15,pady=15,columnspan=3)

browse_button = Button(root, text="Browse", command=Location, width=20, bg = "#b99bd1", relief=GROOVE)
browse_button.grid(row=4,column=2,padx=15,pady=15)

download_button = Button(root, text="Download Video", command=Download_Video, width=50, bg="#9bcdd1",relief=GROOVE)
download_button.grid(row=4, column=1,padx=15,pady=15)

functionality()
root.mainloop()