💬 Python Chat Application (Client-Server)



A simple real-time chat application built with Python sockets and Tkinter GUI.

It allows multiple clients to connect to a server and exchange messages in a chatroom interface.



✨ Features



Server GUI – displays connected clients and chat logs



Multiple Clients – supports many users at once



Broadcasting – messages from one client are sent to all others



Join/Leave Alerts – notifies when a client connects or disconnects



GUI Input – send messages via a text box + send button



Multithreading – handles multiple clients simultaneously



📂 Project Structure



client-server/

├── server.py # Chat server with Tkinter GUI

├── client.py # Chat client with Tkinter GUI

└── README.md # Project documentation







\### Client

!\[Client Screenshot](screenshots/client.png)



\### Server

!\[Server Screenshot](screenshots/server.png)



🚀 How to Run



Start the Server

python server.py



Start Clients

In another terminal (or another computer on the same network):

python client.py



You can run multiple clients to test group chat.



⚙️ Requirements



Python 3.x



Tkinter (comes preinstalled with Python on most systems)



🔮 Future Improvements



Add username/password authentication



Private messages (direct messaging)



File sharing (send images, docs, etc.)



Better GUI design (dark mode, user list panel)

