import socket
import threading
import tkinter as tk

# Define the host and port
host = 'localhost'
port = 8000

# Create a new socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((host, port))

# Function to handle receiving messages from the server


def receive_messages():
    while True:
        # Receive data from the server
        data = client.recv(1024).decode()

        # Update the chat log with the new message
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END,''+ data + '\n')
        chat_log.config(state=tk.DISABLED)


def send_message(event=None):
    # Get the message from the input box
    message = input_box.get()

    # Append the message to the chat log
    chat_log.configure(state=tk.NORMAL)
    chat_log.insert(tk.END, '')
    chat_log.configure(state=tk.DISABLED)

    # Send the message to the server
    client.sendall(message.encode())

    # Clear the input box
    input_box.delete(0, tk.END)

    # Disable the chat log while the message is sendig
    chat_log.config(state=tk.DISABLED)

    # Enable the chat log when message sent
    chat_log.config(state=tk.NORMAL)


# Creating GUI
root = tk.Tk()
root.title('Chat Application for User-1')

# Creatin chat log
chat_log = tk.Text(root, bg='#a3d7e2', state=tk.DISABLED)

# chat_log = tk.Text(root, state=tk.DISABLED)
chat_log.pack()

# Creating input box
input_box = tk.Entry(root)
input_box.pack()

# Create the send button
send_button = tk.Button(root, text='Send', command=send_message, fg='blue')
send_button.pack()

# Bind the return key
input_box.bind('<Return>', lambda event: send_message())

# Start receiving messages from the server in separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start the GUI main loop
root.mainloop()
