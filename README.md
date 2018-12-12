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
__init__(self, host, port)
    Create a socket connection to given host and port.

close(self)
    Closes the socket.

duplicate(self)
    Returns a new socc object of the same host and port.

ignore(self, number_of_lines=1, amount=1024)
    Recieve and ignore the specified amount of lines from the socket.

#Requires telnetlib
interact(self)
    Allows the user to interact with the socket.

recv(self, amount=1024)
    Recieve a string over the socket.

recv_bytes(self, amount=1024)
    Recieve a bytes object over the socket.

send(self, message)
    Send a string over the socket.

send_bytes(self, message)
    Send a bytes object over the socket.
```
