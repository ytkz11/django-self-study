#!/usr/bin/env python
import socket
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''
hello, world!<h1>hello 20230206</h1>
'''
response_params = [
    'HTTP/1.0 200 OK',
    body,
]
response = '\r\n'.join(response_params)

def handle_connection(conn, addr):
    requests = b""
    while EOL1 not in requests and EOL2 not in requests:
        requests +=conn.recv(1024)
    print(requests)
    conn.send(response.encode())
    conn.close()
def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5)
    print('http://127.0.0.1:8000')
    try:
        while True:
            conn, address = serversocket.accept()
            handle_connection(conn, address)
    finally:
        serversocket.close()
if __name__ == '__main__':
    main()