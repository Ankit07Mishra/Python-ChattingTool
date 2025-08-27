import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 12345
nickname = ""

window = tk.Tk()
window.title("Chat Client")
window.geometry("400x500")
window.configure(bg="#222")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, bg="#111", fg="white", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state='disabled')

entry_field = tk.Entry(window, font=("Arial", 12), bg="#333", fg="white")
entry_field.pack(padx=10, pady=(0, 5), fill=tk.X)

send_button = tk.Button(window, text="Send", bg="green", fg="white", font=("Arial", 12, "bold"), command=lambda: send_message())
send_button.pack(padx=10, pady=(0, 10), fill=tk.X)

def display_message(msg):
    chat_area.config(state='normal')
    chat_area.insert(tk.END, msg + "\n")
    chat_area.yview(tk.END)
    chat_area.config(state='disabled')

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message != 'NICK':
                display_message(message)
        except:
            client.close()
            break

def send_message():
    msg = entry_field.get()
    if msg:
        full_msg = f"{nickname}: {msg}"
        client.send(full_msg.encode())
        display_message(full_msg)  # show your own message too
        entry_field.delete(0, tk.END)

def on_close():
    client.close()
    window.destroy()

nickname = simpledialog.askstring("Nickname", "Enter your nickname:", parent=window)
if not nickname:
    exit()

try:
    client.connect((HOST, PORT))
    client.send(nickname.encode())
except:
    display_message("❌ Cannot connect to the server.")
    exit()

threading.Thread(target=receive, daemon=True).start()

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
