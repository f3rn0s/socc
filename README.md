# socc

Socc is designed to provide a simple little wrapper for the creation and management of a connection-based socket.
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

#### Socket Extras


