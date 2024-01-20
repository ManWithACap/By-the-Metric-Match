# Welcome to the main entrypoint of the app!
# Enjoy your stay and grab a byte to eat! Make yourself at home!

import tkinter as tk
import os, random

root = tk.Tk()
startX = int((root.winfo_screenwidth() / 2) - 250)
startY = int((root.winfo_screenheight() / 2) - 250)
root.geometry(f"500x500+{startX}+{startY}")
root.title("By the Metric Match")

label = tk.Label(root, text="Hello, World!")
label.pack()

def buttonClick():
    global timesClicked
    timesClicked += 1
    print("Button clicked!")
    buttonLabel.config(text="Logged in terminal " + str(timesClicked) + " times.")
timesClicked = 0
button = tk.Button(root, text="Click me!", command=buttonClick)
button.pack()

buttonLabel = tk.Label(root, text="")
buttonLabel.pack()

def createButtonClick():
    global newWindows
    newWindows += 1
    cbLabel.config(text="Number of new windows: " + str(newWindows))

    root2 = tk.Toplevel(root)
    root2.title("New Window")
    r2StartX = random.randint(0, root.winfo_screenwidth() - 1)
    r2StartY = random.randint(0, root.winfo_screenheight() - 1)
    root2.geometry(f"100x100+{r2StartX}+{r2StartY}")

    label2 = tk.Label(root2, text="Hello, World!")
    label2.pack()
createButton = tk.Button(root, text="Create new.", command=createButtonClick)
createButton.pack()

newWindows = 0
cbLabel = tk.Label(root, text="")
cbLabel.pack()

root.mainloop()