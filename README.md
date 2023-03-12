# File Sharing Application Overview

The following project follows a basic client-server model which performs as file sharing application that allows clients to upload and download files to/from a server.

See the instructions below on how to run it:

Starting the server:

1. Open a command prompt/terminal window.
2. Navigate to the directory containing the server.py file.
3. Run the following command to start the server:

        python server-side.py

The server should now be running and waiting for connections from clients!

Starting the client:

1. Open a command prompt/terminal window.
2. Navigate to the directory containing the client.py file.
3. Run the following command to start the client:

        python client-side.py

The client should now be running and waiting for user input!

Using the client:


- To upload a file to the server, type the following command and press Enter.

        upload <filename>
        
If the file does not exist on the server, it will be uploaded. If the file already exists on the server, you will receive an error message.

- To download a file from the server, type the following command and press Enter.

        download <filename> 
        
If the file exists on the server, it will be downloaded and saved to your local machine. If the file does not exist on the server, you will receive an error message.

To exit the client, type exit and press Enter.

<br>

My purpose for writing this software was to provide a way to transfer files between machines without the use of internet or a USB.


[Software Demo Video](https://www.loom.com/share/70a261f1a55e4b7f97fa10f030849ed4)

# Network Communication

Architecture:

The program follows a client-server architecture. The server is responsible for managing the files and processing requests from the clients, while the clients can upload and download files from the server.
<br><br>
Transport Protocol:

The program uses the TCP protocol for reliable data transmission. This is because file transfers require guaranteed delivery of data without any loss or corruption.
<br><br>
Port numbers:

The server listens for incoming connections on a specific port number, which is set to 2222 in the program. This port number can be changed if needed.
<br><br>
Message Format:

The program uses a simple text-based message format for communication between the client and server. The messages are formatted as strings with a command and an argument separated by a space. Note that the messages are encoded using UTF-8 before being sent over the network.
# Development Environment

The software was developed using Visual Studio Code and the basic command-line terminals of my test machines. For testing, I used a Windows 10 PC and a Linux VM.

All files were written in Python including the following built-in modules:
- [socket](https://docs.python.org/3/library/socket.html): creating and managing network sockets to allow communication between the client and server
- [os](https://docs.python.org/3/library/os.html): for file operations like creating and deleting files
- [os.path](https://docs.python.org/3/library/os.path.html): for checking if a file exists on the server and getting the size of a file
- [sys](https://docs.python.org/3/library/sys.html): exiting the client

# Useful Websites

* [File Transfer using TCP Socket in Python3](https://idiotdeveloper.com/file-transfer-using-tcp-socket-in-python3/)

# Future Work

* Functionality to edit files on either side
* Functionality to perform actions (enter commands) on either side
* Encrypt/decrypt data sent