import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Rahul" and password == "3100py":
        messagebox.showinfo("Login Successful", "Welcome, Rahul!")
        login_window.destroy()
        os.environ["ALLOW_MAIN_EXECUTION"] = "true"  # Set the environment variable
        subprocess.call(["python", "main.py"])
    else:
        messagebox.showerror("Login Failed", "Incorrect password. Please try again.")
        username_entry.delete(0, tk.END)  # Clear username entry
        password_entry.delete(0, tk.END)

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry('400x200')
login_window.iconbitmap('read.ico')

login_frame = tk.Frame(login_window)
login_frame.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:", font=("Georgia", 12))
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame, font=("Times New Roman", 12))
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(login_frame, text="Password:", font=("Georgia", 12))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show="*", font=("Times New Roman", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(login_frame, text="Login", font=("Gill Sans MT", 13), bg='#EF9595', command=check_login)
login_button.grid(row=2, columnspan=2, pady=20)

login_window.mainloop()