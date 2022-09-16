from multiprocessing.connection import Client
from command import *
from server_crypt import *
import socket                   

port = 60000                    # Reserve a port for your service.
# Create a socket object
server_socket = socket.socket()             
host = socket.gethostname()                 # Get local machine name
server_socket.bind((host, port))            # Bind to the port
server_socket.listen(5)                     # Now wait for client connection.

print('Server is listening....')

# Establish connection with client using a while loop
while True:
   # receiving the request from client
   conn, addr = server_socket.accept()     
   print('Successfully got the connection from', addr)
   command = conn.recv(1024)
   command = command.decode()

   encryption = conn.recv(1024)
   encryption = encryption.decode()

   command = decrypt(command, encryption) 
   print('Server received - \n', 'Command: ', command, '\n', 'Mode of encryption: ', encryption)

   # command handle
   command_response, status = commands(command, encryption)
   server_response = encrypt(command_response, encryption)
   server_response = server_response.encode()
   server_status = encrypt(status, encryption)
   server_status = server_status.encode()

   # send the response to client
   conn.send(server_response)
   conn.send(server_status)

   print('Request successfully sent.')
   print('***********************************')
   conn.close()
