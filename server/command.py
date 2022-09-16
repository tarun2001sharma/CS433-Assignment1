import os
from server_crypt import * 

def commands(encrypted_command, mode):
    
    command = encrypted_command.strip()
    response = ""
    status = ""

    print("server command is running: ", command)
    
    if (command == 'cwd' or command == 'CWD'):
        response = os.getcwd()
        status = "OK"

    elif (command == 'ls' or command == 'LS'):
        response = "Directory List: \n"
        for i in os.listdir():
            response += i + "\n"
            status = "NOK"

    elif (command.split(' ')[0] == "cd" or command.split(' ')[0] == "CD"):
        try:
            path = command[3:]
            os.chdir(path)
            curr_dir = os.getcwd()
            response = 'Directory has been changed to ' +  curr_dir
            status = "OK"
        except:
            response = 'Directory does not exist!'
            status = "NOK"

    elif (command.split(' ')[0] == "dwd" or command.split(' ')[0] == "DWD"):
        try:
            path = command[4:]
            f = open(path, 'r')
            response = f.read(2048)
            f.close()
            status = "OK"
        except:
            response = 'File does not exist!'
            status = "NOK"

    elif (command.split(' ')[0] == "upd" or command.split(' ')[0] == "UPD"):
        try:
            if(len(command) < 4):
                raise Exception()
            data = command[4:]
            f = open('uploaded_file.txt', 'w')
            f.write(data)
            f.close()
            response = "File has been uploaded to server."
            status = "OK"
        except:
            response = 'File could not be uploaded!'
            status = "NOK"

    else:
        response = "Command not available."
        status = "NOK"

    return response, status