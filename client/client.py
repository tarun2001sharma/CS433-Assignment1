import socket                   # Import socket module
from __init__ import *
from client_crypt import *

# Create a socket object
client_socket = socket.socket()             
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

client_socket.connect((host, port))
# s.send("Hello server!".encode())
command, encryption = enter_command()
print(command, encryption)
command = encrypt(command, encryption)
# encryption
client_socket.send(command.encode())
client_socket.send(encryption.encode())

# Response from the server
data_response = client_socket.recv(1024)
data_response = data_response.decode()
status_response = client_socket.recv(1024)
status_response = status_response.decode()

data_response = decrypt(data_response, encryption)
status_response = decrypt(status_response, encryption)

print("Data Response: ", data_response)
print("Status Response: ", status_response)

client_socket.close()
print('connection closed')


# with open('received_file', 'w') as f:
#     print('file opened')
#     while True:
#         print('receiving data...')
#         data = s.recv(1024)
#         data = data.decode()
#         print(data)
#         if not data:
#             break
#         # write data to a file
#         f.write(data)

# f.close()
# print('Successfully get the file')
# s.close()
# print('connection closed')