# socc

Socc is a simply library designed to provide a simple wrapper for the creation and management of connection-based sockets.
It just makes the code a tiny bit cleaner.

#### socc vs socket

##### socc
```python3
import socc

hostname = '127.0.0.1'
port = 80

s = socc.socc(hostname, port)

x = s.recv()

s.send('Hello World!')

s.close()
```

##### socket
```python3
import socket

hostname = '127.0.0.1'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))

x = s.recv(1024).decode()

s.send('Hello World!'.encode('utf-8'))

s.close()
```

#### Socc Functions

```
__init__(self, host: str, port: int) -> None
    Create a socket connection to given host and port.

close(self) -> None
    Closes the socket.

duplicate(self)
    Returns a new socc object of the same host and port.

ignore(self, number_of_lines: int = 1, bufsize: int = 1024) -> None
    Recieve and ignore the specified bufsize of lines from the socket.

interact(self) -> None
    Allows the user to interact with the socket.

recv(self, bufsize=1024) -> str
    Recieve a string over the socket.

recv_bytes(self, bufsize: int = 1024) -> bytes
    Recieve a bytes object over the socket.

send(self, message: str) -> None
    Send a string over the socket.

send_bytes(self, message: bytes) -> None
    Send a bytes object over the socket.

set_line_ending(self, lineending: str) -> None
    Change the default line ending
```
