import socket

HOST = 'localhost'
PORT = 8000
OUT_FILE = 'output'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print 'Connected by', addr

output = open(OUT_FILE, 'w')
while 1:
    data = conn.recv(1024)
    if not data: break
    output.write(data)

output.flush()
output.close()
conn.close()
