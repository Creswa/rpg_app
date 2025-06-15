import tkinter as tk
from tkinter import ttk

def skill_create():
    print(new_skill_name.get())

new_skill_name = tk.StringVar(value = "Enter skill name") #string_var in the Add skill entrs field

# window
window = tk.Tk()
window.title('RPG app')
window.geometry('600x600')
window.minsize(400, 400)
window.resizable(True, True)

#layout frames
frame_top = ttk.Frame(window, height = 50, borderwidth = 10)
frame_top.pack_propagate(False)
frame_top.pack(side = "top", fill = "both", expand = True)

frame_bottom = ttk.Frame(window, height = 200, borderwidth = 10)
frame_bottom.pack_propagate(False)
frame_bottom.pack(side = "top", fill = "both", expand = True)

frame3 = ttk.Frame(window, height = 50, borderwidth = 10)
frame3.pack_propagate(False)
frame3.pack(side = "bottom", fill = "both", expand = True, anchor= "center")

##grid setups

#top frame grid setup
frame_top.columnconfigure((0,1), weight = 1, uniform="a")
frame_top.columnconfigure(2, weight = 2)

#bottom frame grid setup
frame_bottom.columnconfigure(0, weight = 2)
frame_bottom.columnconfigure((1,2), weight = 1, uniform="a")

## widgets
# top frame
name = tk.Label(frame_top, text = 'Name:', background = 'red', anchor = "w").grid(column = 0, sticky = "nsew")
level = tk.Label(frame_top, text = 'Level:', background = "purple", anchor = "w").grid(row = 0, column = 1, sticky = "nsew")

#centre frame
skills = tk.Label(frame_bottom, text = 'Skills', background = 'blue').pack(expand = True, fill = 'both')

#bottom frame
skill_name = ttk.Entry(frame3, textvariable = new_skill_name).grid(column = 0, sticky = "nsew")
add_skill_button = ttk.Button(frame3, text = 'Add skills', command = skill_create).grid(row = 0, column = 1, sticky = "nsew")
delete_mode_button = ttk.Button(frame3, text = 'Delete mode').grid(row = 0, column =2, sticky = "nsew")


# run
window.mainloop()
