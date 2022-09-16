from multiprocessing.connection import Client
from command import *
from server_crypt import *
import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
# Create a socket object
server_socket = socket.socket()             
host = socket.gethostname()     # Get local machine name
server_socket.bind((host, port))            # Bind to the port
server_socket.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
   conn, addr = server_socket.accept()     # Establish connection with client.
   print('Got connection from', addr)
   command = conn.recv(1024)
   command = command.decode()
   print(command)

   encryption = conn.recv(1024)
   encryption = encryption.decode()

   print("Before:", command)
   command = decrypt(command, encryption)
   print('Server received - \n', 'Command: ', command, '\n', 'Mode of encryption: ', encryption)

   command_response, status = commands(command, encryption)
   server_response = encrypt(command_response, encryption)
   server_response = server_response.encode()
   server_status = encrypt(status, encryption)
   server_status = server_status.encode()

   conn.send(server_response)
   conn.send(server_status)

   print('Done sending')
#  conn.send('Thank you for connecting'.encode())
   conn.close()
