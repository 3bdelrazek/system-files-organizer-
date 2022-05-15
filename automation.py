# import library
import os
import shutil
from tkinter import *
from tkinter import filedialog

# initializing tkinter
app = Tk()
app.title("Organize your Files ")
app.geometry("400x350",)
lb1 = Label(text="⁘ Welcome ⁘  ",font= ("Tahoma",25),fg="#9720ff").pack()

# open function
def openfolder():
    global current
    app.filename = filedialog.askdirectory(initialdir="D:/", title="select folder")
    current = app.filename

# sorting function
def organize():
    # make a directory
    folders_name = ["Images", "Music", "Videos", "PSD Files", "Ai Files", "Pdf & Doc", "Excel Files", "ZIP Files"]
    for folder in folders_name:
        if not os.path.exists(current + "/" + folder):
            os.mkdir(current + "/" + folder)

    for filename in os.listdir(current):
        source = current + "/" + filename
        # check the Extensions of files
        if filename.endswith((".png", ".jpg", ".jpge")):
            shutil.copy(source, current + "/" + "Images")
            os.remove(source)
        if filename.endswith((".mp3", ".wav")):
            shutil.copy(source, current + "/" + "Music")
            os.remove(source)
        if filename.endswith((".mp4", ".mov", ".avi")):
            shutil.copy(source, current + "/" + "Videos")
            os.remove(source)
        if filename.endswith(".psd"):
            shutil.copy(source, current + "/" + "PSD Files")
            os.remove(source)
        if filename.endswith((".ai", ".esp")):
            shutil.copy(source, current + "/" + "Ai Files")
            os.remove(source)
        if filename.endswith((".zip", ".rar")):
            shutil.copy(source, current + "/" + "ZIP Files")
            os.remove(source)
        if filename.endswith((".pdf", ".docx")):
            shutil.copy(source, current + "/" + "Pdf & Doc")
            os.remove(source)
        if filename.endswith((".xlsx", ".csv")):
            shutil.copy(source, current + "/" + "Excel Files")
            os.remove(source)
    Label(text=f"compeleted successfully ", font=("Tahoma", 25), fg="#ff5166").pack()


grid1 = Label(text="⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴",font= ("Tahoma",20),fg="#ff5166").pack()
button1 = Button(app, text="Open Folder",font= ("Lucida",20), command=openfolder,fg="white", bg="#c481ff")
button1.pack()
grid2 = Label(text="⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴",font= ("Tahoma",20),fg="#ff5166").pack()
button2 = Button(app, text="Start Cleaning",font= ("Lucida",20), command=organize,fg="white", bg="#c481ff")
button2.pack()
Name = Label(text="◉Designed By® Abdelrazek Elsayad ",font= ("Tahoma",15),fg="#6c61ff").pack()
linkedin = Label(text="▣ linkedin.com/in/abdelrazek-elsayad ",font= ("Tahoma",15),fg="#6c61ff").pack()

app.mainloop()

