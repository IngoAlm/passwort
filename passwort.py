#!/usr/bin/env python3

# Das Programm erstellt ein zufälliges Passwort mit eingegebener Länge.

import tkinter as tk
import random
import string
import tkinter.font as tkFont

root = tk.Tk()
root.title("Passwortgenerator")
root.geometry("400x200")
root.option_add("*Font", tkFont.Font(family="Arial", size=64))

len_var = tk.IntVar(value=12)

tk.Label(root, text="Länge:").pack(padx=(10, 0))
tk.Spinbox(root, from_=12, to=32, textvariable=len_var, width=5).pack()

out = tk.Entry(root, width=25, justify="center")
out.pack(pady=8)

def gen():
    n = int(len_var.get())
    zeichen = string.ascii_letters + string.punctuation + string.digits
    pwd = ""
    for i in range(n):
        pwd += random.choice(zeichen)
    out.delete(0, "end")
    out.insert(0, pwd)

def copy():
    root.clipboard_clear()
    root.clipboard_append(out.get())

tk.Button(root, text="generieren", command=gen).pack(pady=4)
tk.Button(root, text="kopieren", command=copy).pack()

root.mainloop()
