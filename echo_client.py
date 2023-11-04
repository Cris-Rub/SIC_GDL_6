import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.3', 999)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b'It is very long message but will only be transmitted in chunks of 16 bytes'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()