import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('RPG app')
window.geometry('600x600')
window.minsize(400, 400)
window.resizable(True, True)

#frame
new_skill_frame = ttk.Frame(window, height = 50, borderwidth = 5, relief="solid")
new_skill_frame.pack_propagate(False)
new_skill_frame.pack(side = "top", fill = "x", expand = True)

#frame grid
new_skill_frame.columnconfigure((0,1), weight = 2)
new_skill_frame.columnconfigure((2,3), weight = 1, uniform="a")
new_skill_frame.rowconfigure((0,1), weight=1)

skill_name = ttk.Label(new_skill_frame, text="Název", anchor="w", borderwidth=1, relief="solid").grid(column = 0, sticky = "nsew")
level = ttk.Label(new_skill_frame, text="Level", anchor="w", borderwidth=1, relief="solid").grid(row = 0, column = 1, sticky = "nsew")
mninus_button = ttk.Button(new_skill_frame, text="+").grid(row = 0, column = 2, sticky = "nsew")
plus_button = ttk.Button(new_skill_frame, text="-").grid(row = 0, column = 3, sticky = "nsew")
level_bar = ttk.Label(new_skill_frame, text="Level progress", anchor="center", borderwidth=2, relief="solid").grid(row = 1, column = 0, columnspan = 4, sticky = "nsew")


window.mainloop()
