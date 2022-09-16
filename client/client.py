import socket                   # Import socket module
from __init__ import *
from client_crypt import *

# Create a socket object
client_socket = socket.socket()             
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

client_socket.connect((host, port))

# Takes in the command from client
# -> encryption with the provided 3 modes - Plain text, Transpose, Substitute
# -> command line with provided 5 commands - cwd, ls, cd, dwd, upd
command, encryption = enter_command()

# check for 'upd' command - if the file is to be uploaded
if(command.split(' ')[0] == "UPD"):
  try:
      source = command.split(' ', 1)
      f = open(source[1], 'r')
      command = "UPD "
      command += f.read(2048)
      f.close()
  except:
      command = "UPD"

  # Encrypt the requested service and send it to server
  encrypted_service = encrypt(encrypt, command)

command = encrypt(command, encryption)

# Send client request to the server
client_socket.send(command.encode())
client_socket.send(encryption.encode())

# Taking the response from the server
data_response = client_socket.recv(1024)
data_response = data_response.decode()
status_response = client_socket.recv(1024)
status_response = status_response.decode()

data_response = decrypt(data_response, encryption)
status_response = decrypt(status_response, encryption)

# check for 'dwd'command, if a file is to be downloaded
check = command.split(' ')[0]

if(check == "dwd" and status_response == "OK"):
  try:
    f = open('file_download.txt', 'w')
    f.write(data_response)
    f.close()
  except:
    response = "Download failed. Please check and try again later."
    status_response = "NOK"

print("Data Response: ", data_response)
print("Status Response: ", status_response)

client_socket.close()

print("CONNECTION TERMINATED")
print("****************************")
