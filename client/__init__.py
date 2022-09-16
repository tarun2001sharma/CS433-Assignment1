from client_crypt import *

def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))

def enter_command():
   
    # command = input()

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

    print(
    '''
    The following are the 5 commands the client can perform:
    CWD         Retrieve the path of the current working directory for the user
    LS          List the files/folders present in the current working directory
    CD <dir>    Change the directory to <dir> as specified by the client            OK/NOK
    DWD <file>  Download the <file> specified by the user on server to client       OK/NOK
    UPD <file>  Upload the <file> on client to the remote server in CWD             OK/NOK
    ''')

    print("Please enter the command in the form:")
    print("<mode of encryption>_<command>_<dir/file/null>")
    
    command_line = input()
    command_line = command_line.split()
    command = listToString(command_line[1:])
    encrypt = str(command_line[0])

    return command, encrypt
