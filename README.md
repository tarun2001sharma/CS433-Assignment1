# CS433-Assignment1

## Network Application using Socket Programming

This code chases to develop a simple remote file system service (RFS) and understand the principles of layered network architecture using sockets in python.

To start the server follow:

```
cd server
python server.py
```

In another terminal window, start the client file, as follows:
```
cd client
python client.py
```

The code is based on 5 types of command services that a client can perform:<br />
    1. cwd - Retrieve the path of the current working directory for the user<br />
    2. ls - List the files/folders present in the current working directory<br />
    3. cd - Change the directory to as specified by the client<br />
    4. dwd - Download the specified by the user on server to client<br />
    5. upd - Upload the on client to the remote server in CWD 
    
The following are some modes to mangle the data before transmitting to the networking layer:<br />
    1. Plain text → No change to the input; (No encryption or decryption)<br />
    2. Substitute → Only alphanumeric characters will be substituted with fixed offset, say Caesar cipher with offset 2. Example ARTZ will be substituted with CTVB<br />
    3. Transpose → Revere the contents in a word by word manner. Example ARTZ will be substituted with ZTRA.<br />
    
To enter a command line as a client, the user needs to specify the mode of encryption and the specific command with file location or directory (if needed).
```
# the command must be of the form: <mode of encryption>_<command>_<dir/file/null>
# Please enter the command in the form:
3 upd D:\Assignment1\client\file_download.txt
```

It is to be noted that the connection between the client and the server is thus non-persistent in nature.
In order to re-establish the client-server connection and view the results of more supported commands, the user can restart the client.
