import socket

HOST = '192.168.56.101' # server IP address
PORT = 22222 # server port number
BUFFER_SIZE = 4096 # buffer size for file transfer

def handle_request(conn):
    '''
    reads in whether the user wants to upload or download a file and responds accordingly
    '''
    request = conn.recv(BUFFER_SIZE).decode('utf-8')
    request_parts = request.split()
    if request_parts[0] == 'UPLOAD':
        filename = request_parts[1]
        #writes contents sent from client to new file
        with open(filename, 'wb') as f:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
        print(f'{filename} uploaded')
    elif request_parts[0] == 'DOWNLOAD':
        filename = request_parts[1]
        #reads in content of file and sents to client
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                conn.sendall(data)
        print(f'{filename} downloaded')
    conn.close()

def main():
    '''
    initiates socket connection and waits for a response from client
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Server is listening on port {PORT}...')
        while True:
            conn, addr = s.accept()
            print(f'Connected by {addr}')
            handle_request(conn)

if __name__ == '__main__':
    main()
