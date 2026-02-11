import tkinter as tk

window = tk.Tk()
window.title("Student Profile")
window.geometry("600x600")
window.resizable(False,False)
window.configure(bg= "purple", cursor = "hand2")

title = tk.Label(window,
                text = "Student Profile",
                font = ("Arial", 13), fg = "black", anchor = "center",)
title.pack(padx= 50, pady = 50)

Name = tk.Label(window,
                text = "Name : Christian L. Igloria ",
                font = ("Arial", 13), fg = "black", anchor = "w",width=100)
Name.pack(padx= 50, pady = 10)
age = tk.Label(window,
                text = "Age : 21 years old",
                font = ("Arial", 13), fg = "black", anchor = "w",width=100)
age.pack(padx= 50, pady = 10)
course = tk.Label(window,
                text = "Course : BSIT",
                font = ("Arial", 13), fg = "black", anchor = "w",width=100)
course.pack(padx= 50, pady = 10)
bday = tk.Label(window,
                text = "Birthday : October 23,2004",
                font = ("Arial", 13), fg = "black", anchor = "w",width=100)
bday.pack(padx= 50, pady = 10)
motto = tk.Label(window,
                text = "Trust the Process",
                font = ("Arial", 10), fg = "black", anchor = "w",width=100)
motto.pack(padx= 50, pady = 10)
window.mainloop()
