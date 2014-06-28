import socket
from PIL import Image as pil
from cStringIO import StringIO
from SimpleCV import Image, Display

display = Display()

HOST = '192.168.2.19'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print 'Connected by', addr

while 1:
    b = ''
    while 1:
        data = conn.recv(1024)
        if not data: break
        b += data
    
    if len(b) > 0:
        img = Image(pil.open(StringIO(b)))
        img.save(display)
