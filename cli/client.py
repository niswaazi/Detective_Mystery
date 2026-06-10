import socket
import threading

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

name = input(
    "Masukkan nama detektif: "
)

client.send(
    f"LOGIN:{name}".encode()
)


def receive():

    while True:

        try:

            message = client.recv(
                4096
            ).decode()

            print(
                "\n" + message
            )

        except:

            print(
                "Koneksi terputus."
            )

            break


def send():

    while True:

        msg = input("> ")

        client.send(
            msg.encode()
        )


threading.Thread(
    target=receive,
    daemon=True
).start()

send()