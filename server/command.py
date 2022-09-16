import os
from server_crypt import * 

def commands(encrypted_command, mode):
    
    command = encrypted_command.strip()
    response = ""
    status = ""

    print("The command", command, "is running")
    
    if (command == 'cwd'):
        response = os.getcwd()
        status = "OK"

    elif (command == 'ls'):
        s = "Files located in the current working directory: \n"
        response = ""
        for i in os.listdir():
            status = "NOK"
            response += i 
            response += "\n"
            
    elif (command.split(' ')[0] == "cd"):
        try:
            path = command[3:]
            s = "Directory has been changed to "
            os.chdir(path)
            dir_change = os.getcwd()
            response = s +  dir_change
            status = "OK"
        except:
            response = "Directory specified does not exist. Please check and try again later."
            status = "NOK"

    elif (command.split(' ')[0] == "dwd"):
        try:
            path = command[4:]
            f = open(path, 'r')
            response = f.read(2048)
            f.close()
            status = "OK"
        except:
            status = "NOK"
            response = "File path does not exist. Please check and try again later."

    elif (command.split(' ')[0] == "upd"):
        try:
            data = command[4:]
            f = open('file_upload.txt', 'w')
            f.write(data)
            f.close()
            status = "OK"
            response = "Your file has been uploaded to the remote server."
        except:
            status = "NOK"
            response = "Your file could not be uploaded."

    else:
        response = "Command not available. Please check and try again later."
        status = "NOK"

    return response, status