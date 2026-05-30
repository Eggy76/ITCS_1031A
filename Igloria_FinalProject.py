import tkinter as tk
from tkinter import ttk, messagebox
import openpyxl as op


window = tk.Tk()
window.title("Medical Appointment System")
window.configure(bg="Pink")

# Form Title
title = tk.Label(window, text="Medical Appointment System", font=("Times New Roman", 14, "bold"), bg="lightgreen")
title.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Frame
genframe = tk.Frame(window, bg="lightgray", bd=2, relief="groove")
genframe.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

# Field labels and entries
cname_label = tk.Label(genframe, text="Name", font=("Poppins", 10, "italic"), bg="lightgray")
cname_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

cname_entry = tk.Entry(genframe, font=("Poppins", 12), width=30)
cname_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

Time_label = tk.Label(genframe, text="Time", font=("Poppins", 10, "italic"), bg="lightgray")
Time_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

Time_entry = tk.Entry(genframe, font=("Poppins", 12), width=30)
Time_entry.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")

qty_label = tk.Label(genframe, text="Date", font=("Poppins", 10, "italic"), bg="lightgray")
qty_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

qty_entry = tk.Entry(genframe, font=("Poppins", 12), width=30)
qty_entry.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")

Service_label = tk.Label(genframe, text="Service", font=("Poppins", 10, "italic"), bg="lightgray")
Service_label.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")

Service_entry = tk.Entry(genframe, font=("Poppins", 12), width=30)
Service_entry.grid(row=7, column=0, padx=10, pady=(0, 10), sticky="w")

# Button callbacks

def clear_fields():
    cname_entry.delete(0, tk.END)
    Time_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)
    Service_entry.delete(0, tk.END)


def submit_record():
    name = cname_entry.get().strip()
    time = Time_entry.get().strip()
    date = qty_entry.get().strip()
    service = Service_entry.get().strip()

    if not (name and time and date and service):
        messagebox.showwarning("Submit", "Please fill in all fields.")
        return

    record_id = len(table.get_children()) + 1
    table.insert("", "end", values=(record_id, name, time, date, service, "Scheduled"))
    clear_fields()


def delete_record():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Delete", "Please select a record to delete.")
        return

    for item in selected:
        table.delete(item)
    clear_fields()


def update_record():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Update", "Please select a record to update.")
        return

    name = cname_entry.get().strip()
    time = Time_entry.get().strip()
    date = qty_entry.get().strip()
    service = Service_entry.get().strip()

    if not (name and time and date and service):
        messagebox.showwarning("Update", "Please fill in all fields before updating.")
        return

    for item in selected:
        values = list(table.item(item, "values"))
        values[1] = name
        values[2] = time
        values[3] = date
        values[4] = service
        table.item(item, values=values)

    clear_fields()


def on_record_select(event):
    selected = table.selection()
    if not selected:
        return

    values = table.item(selected[0], "values")
    if values:
        cname_entry.delete(0, tk.END)
        cname_entry.insert(0, values[1])
        Time_entry.delete(0, tk.END)
        Time_entry.insert(0, values[2])
        qty_entry.delete(0, tk.END)
        qty_entry.insert(0, values[3])
        Service_entry.delete(0, tk.END)
        Service_entry.insert(0, values[4])

# Buttons
button_frame = tk.Frame(genframe, bg="lightgray")
button_frame.grid(row=8, column=0, padx=10, pady=(10, 10), sticky="w")

submit_btn = tk.Button(button_frame, text="Submit", font=("Poppins", 12, "bold"), bg="white", command=submit_record)
submit_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(button_frame, text="Update", font=("Poppins", 12, "bold"), bg="blue", command=update_record)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Delete", bg="red", fg="white", font=("Poppins", 12, "bold"), command=delete_record)
delete_btn.grid(row=0, column=2, padx=5)

# Table
table = ttk.Treeview(
    window,
    columns=("Appointment List", "Name", "Time", "Date", "Service", "Result"),
    show="headings"
)

for headings in ("Appointment List", "Name", "Time", "Date", "Service", "Result"):
    table.heading(headings, text=headings)

table.grid(row=1, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
table.bind("<<TreeviewSelect>>", on_record_select)

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()
