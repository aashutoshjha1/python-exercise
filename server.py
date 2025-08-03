#!/usr/bin/env python3

import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 3000))
server_socket.listen(1)

print("server is listening on port 3000")


conn, addr = server_socket.accept()
print(f"connected with addr : {addr} and connection : {conn}")

while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   print(f"client data {data}")
   conn.send(f"received data : {data} ".encode())

conn.close()



