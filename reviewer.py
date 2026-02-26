import tkinter as tk

window = tk.Tk()

window.title("First Window")
window.geometry("500x500")
window.resizable(True,True)
window.configure(bg= "White", cursor="arrow")

label = tk.Label(window,text="Hi",bg="blue",font=("Poppins", 25,"bold"))
label.pack(pady=5)

frame = tk.Frame(window,bg="pink")
frame.pack()

name_label=tk.Label(window,text="Hi",bg="green",font=("Poppins", 16,"bold"))
name_label.pack()

name_entry = tk.Entry(frame)
name_entry.pack(padx=10,pady=10)

pw_label=tk.Label(window,text="Hi",bg="green",font=("Poppins", 16,"bold"))
pw_label.pack()

pw_entry = tk.Entry(frame,show="*")
pw_entry.pack(padx=10,pady=10)

listbox_lbl = tk.Label(frame,text= "choose")
listbox_lbl.pack()

listbox = tk.Listbox(frame,selectmode="single")
listbox.insert(0,"Python")
listbox.insert(1,"Java")
listbox.insert(2,"C#")
listbox.insert(3,"Perl")

window.mainloop()
