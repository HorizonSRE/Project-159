from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x600")
root.title("thingy")
dict_flag={"Country":"1"}
try: print(dict_flag["India"])
except KeyError():
    messagebox.function_name("Key Error" , "Error")
root.mainloop()