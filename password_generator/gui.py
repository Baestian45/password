import tkinter as tk
from tkinter import messagebox
import random
import string

def generated_password(characters):
    alle_zeichen = string.ascii_letters + string.digits
    password = ""
    for _ in range(characters):
        password_stelle = random.randint(0, len(alle_zeichen) - 1)
        password_neues_zeichen = alle_zeichen[password_stelle]
        password = password + password_neues_zeichen
    return password

def generate_password():
    try:
        characters = int(entry.get())
        if characters <= 0:
            raise ValueError("Number of characters must be positive.")
        global password
        password = generated_password(characters)
        result_label.config(text=f"Your new password is: {password}")
        copy_button.pack(pady=5)
        print(f"\nYour new password is '{password}'\n")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        print("Invalid input, please enter a positive integer.")

def copy_to_clipboard():
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("PyPassword Generator")
root.geometry("400x250")
root.resizable(False, False)

welcome_label = tk.Label(root, text="Welcome to the PyPassword Generator!", font=("Helvetica", 14))
welcome_label.pack(pady=10)

prompt_label = tk.Label(root, text="How many characters would you like in your password?")
prompt_label.pack()

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)

root.mainloop()
