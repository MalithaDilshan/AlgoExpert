import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()  # Top level widget
apps = []
root.resizable(False, False)

file_name_path = 'C:\\App Run\\appNames.txt'

if os.path.isfile(file_name_path):
    with open(file_name_path, 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    new_count = 0
    for new_app in apps:
        new_count += 1
        if new_app:
            tk.Label(frame, text=str(new_count) + " " + new_app, bg="white").grid(column=0, row=new_count, sticky=tk.W)
        # label.pack(anchor="w")
        # label.place(x=5, y=40)


def runApps():
    for app in apps:
        os.startfile(app)


def deleteApps():
    open(file_name_path, 'w').close()
    for widget in frame.winfo_children():
        widget.destroy()
    apps.clear()


canvas = tk.Canvas(root, height=450, width=550, bg="#D9D9FF", highlightthickness=2,
                   highlightbackground="#7777FF")  # Adding a canvas
canvas.pack(fill=tk.BOTH, expand=0)

frame = tk.Frame(root, bg="#C0C0C0", highlightthickness=1.5, highlightbackground="gray")  # Adding a frame into the
# root
frame.place(relwidth=0.9, relheight=0.75, anchor="n", relx=.5, rely=.05)

frame1 = tk.Frame(root, bg="#A1F1A1", highlightthickness=2.3, highlightbackground="#169016")  # Adding a frame into the
# root
frame1.place(relwidth=0.9, relheight=0.1, anchor="s", relx=.5, rely=0.95)

button1 = tk.Button(frame1, text="Open", padx=3, pady=2, fg="black", bg="#1BB21B", width=10, command=addApp)
# button1.pack(expand=0,  padx=50, pady=0.3, anchor="c", side=tk.RIGHT)
button1.place(x=105, y=6)

button2 = tk.Button(frame1, text="Execute", padx=3, pady=2, fg="black", bg="#1BB21B", width=10, command=runApps)
# button2.pack(expand=0,  padx=50, pady=0.3, anchor="c", side=tk.LEFT)
button2.place(x=205, y=6)

button2 = tk.Button(frame1, text="Delete All", padx=3, pady=2, fg="black", bg="#1BB21B", width=10, command=deleteApps)
# button2.pack(expand=0,  padx=50, pady=0.3, anchor="c", side=tk.LEFT)
button2.place(x=305, y=6)

count = 0
for app in apps:
    count += 1
    label = tk.Label(frame, text=str(count) + " " + app, bg="white").grid(column=0, row=count, sticky=tk.W)
    # label.place(x=5, y=40)

root.mainloop()

with open(file_name_path, 'w') as f:
    for app in apps:
        f.write(app + ',')
