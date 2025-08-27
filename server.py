import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = 'localhost'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

window = tk.Tk()
window.title("Chat Server")
window.geometry("400x500")
window.configure(bg="#222")

# Chat display
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, bg="#111", fg="white", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state='disabled')

# Entry field
entry_field = tk.Entry(window, font=("Arial", 12), bg="#333", fg="white")
entry_field.pack(padx=10, pady=(0, 5), fill=tk.X)

# Button
send_button = tk.Button(window, text="Send", bg="red", fg="white", font=("Arial", 12, "bold"))
send_button.pack(padx=10, pady=(0, 10), fill=tk.X)

def display_message(msg):
    chat_area.config(state='normal')
    chat_area.insert(tk.END, msg + "\n")
    chat_area.yview(tk.END)
    chat_area.config(state='disabled')

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                remove_client(client)

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        display_message(f"⚠ {nickname} disconnected")
        clients.remove(client)
        nicknames.pop(index)
        client.close()
        broadcast(f"{nickname} has left the chat.")

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode()
            display_message(message)
            broadcast(message, client)
        except:
            remove_client(client)
            break

def receive():
    while True:
        client, _ = server.accept()
        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        clients.append(client)
        nicknames.append(nickname)
        display_message(f"✅ {nickname} joined the chat")
        broadcast(f"{nickname} joined the chat.")
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def send_message():
    msg = entry_field.get()
    if msg:
        full_msg = f"Server: {msg}"
        display_message(full_msg)
        broadcast(full_msg)
        entry_field.delete(0, tk.END)

send_button.config(command=send_message)
window.bind("<Return>", lambda event: send_message()) 


threading.Thread(target=receive, daemon=True).start()

def on_close():
    for client in clients:
        client.close()
    server.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
