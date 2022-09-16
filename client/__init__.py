from client_crypt import *

def enter_command():
    print(
    '''
    The following are the 5 commands the client can perform:
    CWD         Retrieve the path of the current working directory for the user
    LS          List the files/folders present in the current working directory
    CD <dir>    Change the directory to <dir> as specified by the client            OK/NOK
    DWD <file>  Download the <file> specified by the user on server to client       OK/NOK
    UPD <file>  Upload the <file> on client to the remote server in CWD             OK/NOK
    ''')
    print("Enter the command: ", end =" ")
    command = input()

    print(
    '''
    The following are some modes to mangle the data before transmitting to the networking layer:
    1. Plain text → No change to the input; (No encryption or decryption)
    2. Substitute → Only alphanumeric characters will be substituted with fixed offset,
    say Caesar cipher with offset 2. Example ARTZ will be substituted with CTVB
    3. Transpose → Revere the contents in a word by word manner. Example ARTZ will
    be substituted with ZTRA.
    ''')
    print("Enter the crypt mode \n (1 for Plain text) \n (2 for Transpose) \n (3 for Substitute) : ", end =" ")
    encrypt = input()

    # if(command.split(' ')[0] == "UPD"):
    #     try:
    #         f = open(command.split(' ', 1)[1], 'r')
    #         command = "UPD " + f.read(2048)
    #         # print(command)
    #         f.close()
    #     except:
    #         command = "UPD"

    # # Encrypt the requested service and send it to server
    # encrypted_service = encrypt(encrypt, command)

    return command, encrypt


def service_response(mode, encrypted_service, response):
    response = decrypt(mode, response)
    service = decrypt(mode, encrypted_service)
    if(service.split(' ')[0] == "DWD"):
        try:
            f = open('downloaded_file.txt', 'w')
            data = response.split(' ', 1)[1]
            response = response.split(' ', 1)[0]
            f.write(data)
            f.close()
            print("Response from server: ", response)
        except:
            print("Response from server: NOK")
    else:
        print("Response from server: ", response)