import tkinter as tk
import hashlib

seamless = False

def hash_entry(event):
    txt1 = true1temp.get()
    sha256 = hashlib.sha256(true1temp.encode())
    estr = sha256.hexdigest()
    print(txt1, estr)


def save():
    global true1, true2, false1, false2, true1temp, true2temp, false1temp, false2temp
    false1 = false1temp.get()
    false2 = false2temp.get()
    true1 = true1temp.get()
    true2 = true2temp.get()
    print(true1, true2, false1, false2)


root = tk.Tk()
root.geometry("250x250")
root.title("Ergo-Mag")
root.config(background="grey")

true1temp = tk.StringVar()
true2temp = tk.StringVar()
false1temp = tk.StringVar()
false2temp = tk.StringVar()
true1 = str(tk.StringVar())
true2 = str(tk.StringVar())
false1 = str(tk.StringVar())
false2 = str(tk.StringVar())

trueLabel = tk.Label(text="Non-Precision Applications",
                     font=("Ubuntu", "13", "bold"),
                     bg="grey",
                     fg="blue",
                     )

trueLabel.pack(pady=3,
               padx=3
               )
trueEntryOne = tk.Entry(textvariable=true1temp,
                        width=40,
                        bg="light grey",
                        fg="blue",
                        font=("Ubuntu", "14")
                        )
trueEntryOne.pack(pady=3,
                  padx=3
                  )
trueEntryTwo = tk.Entry(textvariable=true2temp,
                        width=40,
                        bg="light grey",
                        fg="blue",
                        font=("Ubuntu", "14")
                        )
trueEntryTwo.pack(pady=3,
                  padx=3
                  )
falseLabel = tk.Label(text="Precision Applications",
                      font=("Ubuntu", "13", "bold"),
                      bg="grey",
                      fg="blue",
                      )
falseLabel.pack(pady=3,
                padx=3
                )
falseEntryOne = tk.Entry(textvariable=false1temp,
                         width=40,
                         font=("Ubuntu", "14"),
                         bg="light grey",
                         fg="blue",
                         )
falseEntryOne.pack(pady=3,
                   padx=3
                   )
falseEntryTwo = tk.Entry(textvariable=false2temp,
                         width=40,
                         font=("Ubuntu", "14"),
                         bg="light grey",
                         fg="blue",
                         )
falseEntryTwo.pack(pady=3,
                   padx=3
                   )
saveButton = tk.Button(text="save",
                       command=save,
                       font=("Ubuntu", "15", "bold"),
                       width=30,
                       bg="light grey",
                       fg="blue")
saveButton.pack(pady=3,
                padx=3
                )
root.mainloop()


