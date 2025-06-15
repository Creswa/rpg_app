import tkinter as tk

class CustomFrame(tk.Frame):
    def __init__(self, parent, name, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.label = tk.Label(self, text=f"Hello from {name}")
        self.label.pack()

        self.button = tk.Button(self, text=f"Click {name}", command=lambda: print(f"{name} clicked!"))
        self.button.pack()

# Main app
root = tk.Tk()
root.title("Multiple Frames Example")

# Create multiple instances
frame1 = CustomFrame(root, "Frame 1", bg="lightblue")
frame1.pack(padx=10, pady=10, fill="x")

frame2 = CustomFrame(root, "Frame 2", bg="lightgreen")
frame2.pack(padx=10, pady=10, fill="x")

frame3 = CustomFrame(root, "Frame 3", bg="lightyellow")
frame3.pack(padx=10, pady=10, fill="x")

root.mainloop()
