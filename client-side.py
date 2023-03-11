import socket

HOST = '192.168.56.101' # server IP address
PORT = 22222 # server port number
BUFFER_SIZE = 4096 # buffer size for file transfer

def upload_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f'UPLOAD {filename}'.encode('utf-8'))
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                s.sendall(data)
        print(f'{filename} uploaded')

def download_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f'DOWNLOAD {filename}'.encode('utf-8'))
        with open(filename, 'wb') as f:
            while True:
                data = s.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
        print(f'{filename} downloaded')

def main():
    while True:
        print('Choose an option:')
        print('1. Upload file')
        print('2. Download file')
        print('3. Quit')
        choice = input('> ')
        if choice == '1':
            filename = input('Enter filename to upload: ')
            upload_file(filename)
        elif choice == '2':
            filename = input('Enter filename to download: ')
            download_file(filename)
        elif choice == '3':
            break
        else:
            print('Invalid choice')

main()