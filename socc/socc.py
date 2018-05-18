import socket

class socc:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, message):
        self.socket.send(message.encode())

    def recv(self, amount):
        return self.socket.recv(amount).decode()

    def duplicate(self):
        return self.socket.dup()

    def close(self):
        self.socket.close()
