import socket
import telnetlib

class socc:
    """A small wrapper class for socket to provide cleaner code."""

    """Default Line Ending"""
    lineending = "\r\n"

    def __init__(self, host, port):
        """Create a socket connection to given host and port."""
        self._host = host
        self._port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, message):
        """Send a string over the socket."""
        if message[-len(self.lineending):] != self.lineending:
            message += self.lineending
        self.socket.send(message.encode())

    def send_bytes(self, message):
        """Send a bytes object over the socket."""
        if message[-len(self.lineending.encode()):] != self.lineending.encode():
            message += self.lineending.encode()
        self.socket.send(message)

    def recv(self, bufsize=1024):
        """Recieve a string over the socket."""
        return self.socket.recv(bufsize).decode()

    def recv_bytes(self, bufsize=1024):
        """Recieve a bytes object over the socket."""
        return self.socket.recv(bufsize)

    def ignore(self, number_of_lines=1, bufsize=1024):
        """Recieve and ignore the specified bufsize of lines from the socket."""
        for i in range(0, number_of_lines):
            self.socket.recv(bufsize)

    def set_line_ending(self, lineending: str) -> None:
        self.lineending = lineending

    def duplicate(self):
        """Returns a new socc object of the same host and port."""
        return socc(self._host, self._port)

    def interact(self):
        """Allows the user to interact with the socket."""
        t = telnetlib.Telnet()
        t.sock = self.socket
        t.interact()

    def close(self):
        """Closes the socket."""
        self.socket.close()
