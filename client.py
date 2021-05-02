from socket import socket, gethostname, SHUT_WR

s = socket()
host = gethostname()
port = 3399

s.connect((host, port))

print("Sending video..")

with open("video.mp4", "rb") as video:
    buffer = video.read()
    s.sendall(buffer)

print("Done sending..")
s.close()