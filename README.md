# socc

Socc is designed to provide a simple little wrapper for the creation and management of a connection-based socket.

It just makes the code a tiny bit cleaner in the cases I need it

```python3
import socc

hostname = '127.0.0.1'
port = 80

s = socc.socc(hostname, port)
#Compared to s.recv(1024).decode()
x = s.recv()
#Compated to s.send(message.encode())
message = 'example message'
x = s.send(message)

s.close()
```

Example:

```python
#Just some random fake code for an example
import socc

def gen_secret(s, key):
  for i in range(0, 100):
    s.send(key) + chr(i)
    if(s.recv()[10] = 'e'):
      return chr(i)

s = socc.socc('127.0.0.1', 80)
key = s.recv()[:11]
secret = gen_secret(s, key)
print(secret)

```
