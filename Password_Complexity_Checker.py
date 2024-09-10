import re
import tkinter as tk
from tkinter import messagebox
def password_complexity_checker(password):
    length_score=len(password) >=8
    uppercase_score= bool(re.search(r'[A-Z]',password))
    lowercase_score= bool(re.search(r'[a-z]',password))
    number_score= bool(re.search(r'[0-9]',password))
    special_char_score = bool(re.search(r'[!@#$%^&*(),.:"{}|<>?~]',password))
    total_score= length_score + uppercase_score + lowercase_score + number_score + special_char_score 
    if total_score == 5:
        return "Strong Password"
    elif total_score >=3:
        return "Good Password"
    else:
        return "Weak Password"

def check_password_strength():
    password=entry.get()
    strength=password_complexity_checker(password)
    messagebox.showinfo("Password Strength",f"Password Strength: {strength}")

root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x200")

label=tk.Label(root,text="Enter your password:")
label.pack(pady=10)

entry=tk.Entry(root,show="*")
entry.pack(pady=10)

button=tk.Button(root,text="Check Password",command=check_password_strength)
button.pack(pady=10)

root.mainloop()