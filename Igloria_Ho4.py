import tkinter as tk

window = tk.Tk()

window.title("Igloria")
window.geometry("500x300")
window.resizable(False,False)
window.configure(bg= "pink")

frame = tk.Frame(window,bg= "White")
frame.pack()

label = tk.Label(window, text= "Profile Builder",font= ("arial",10,))
label.pack()

name_entry = tk.Entry(window,bg= "white",font= ("white",10,"italic"))
name_entry.place(x=20,y=70)

name = tk.Label(window,text= "First Name",font= ("arial",10,"italic"))
name.place(x=50,y=100)

birth_entry = tk.Entry(window, bg= "white",
font= ("arial",10,"bold"))
birth_entry.place(x=20,y=140)

birth_name = tk.Label(window, text= "Birth Year",
font= ("arial",10, "italic" ))
birth_name.place (x=50,y=170)
button = tk.Button(window, bg= "Pink",text= "Submit", font= ("arial",10,"bold"))
button.place(x=220,y=250)
gender = tk.Label(window, text="Gender", font= ("arial",8, "italic"))
gender.place(x=60,y=200)
male = tk. Radiobutton (window, text="Male")
male.place(x=170,y=200)
female = tk.Radiobutton (window, text="Male")
female.place(x=170,y=200)
middle_entry = tk.Label(window,bg= "white")
middle_entry = tk.Entry(window,
font= ("arial",10,"bold"),)
middle_entry.place (x=180,y=70)

middle_name = tk.Label(window,
text= "Middle Name",
font= ("arial",10, "italic" ))
middle_name.place(x=210,y=100)

last_entry = tk.Entry (window, bg= "white",)
font= ("arial",10,"bold"),

last_entry.place (x=340,y=70)
last_name =tk.Label(window,
text="Last Name",
font= ("arial",10, "italic" )
)
last_name.place(x=380,y=100)


window.mainloop()
