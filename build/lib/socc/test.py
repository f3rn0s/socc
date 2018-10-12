import socc

s = socc.socc('127.0.0.1', 80)

s.send('GET /')

s.recvfrom(1024)
