import tkinter as tk
import subprocess

def open_encryption_ui():
    subprocess.Popen(["python", "encryption_ui.py"])

def open_decryption_ui():
    subprocess.Popen(["python", "decryption_ui.py"])

# GUI setup
root = tk.Tk()
root.title("Text Encryption & Decryption")
root.geometry("300x200")

tk.Label(root, text="Select an option:", font=("Arial", 12)).pack(pady=10)

btn_encrypt = tk.Button(root, text="Encrypt Text", command=open_encryption_ui, width=20)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(root, text="Decrypt Text", command=open_decryption_ui, width=20)
btn_decrypt.pack(pady=5)

root.mainloop()
