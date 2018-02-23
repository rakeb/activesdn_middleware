import socket


def tcp_receiver():
    TCP_IP = '172.16.53.1'
    TCP_PORT = 5556
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print
    'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print("received data:", data)
        conn.send(data)  # echo
    # data = '''HTTP/1.1\r\n 200 OK\r\n\n'''
    # conn.send(bytes(data))  # echo
    conn.close()


if __name__ == '__main__':
    while 1:
        tcp_receiver()
