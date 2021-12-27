import socket
from threading import Thread


class Client:
    def __init__(self, send_host, send_port) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr_send = ('0.0.0.0', send_port)

    def start(self):
        try:
            self.sock.bind(('0.0.0.0', 3000))
        except OSError:
            self.sock.bind(('0.0.0.0', 3030))

        print('Chat is online.')
        print(f'Use {self.sock.getsockname()} to chat.\n')

        recv = self.receive_message
        recv_thread = Thread(target=recv)

        send = self.send_message
        send_thread = Thread(target=send)

        send_thread.start()
        recv_thread.start()

    def receive_message(self) -> None:
        while True:
            message, addr = self.sock.recvfrom(5012)
            print(f'\033[1m{addr[0]}/{addr[1]}: {message.decode()}\033[m')

    def send_message(self) -> None:
        while True:
            message = input('>> \r').strip()
            self.sock.sendto(message.encode(), self.addr_send)

    
chat = Client('0.0.0.0', int(input('Port to chat: ')))
chat.start()
