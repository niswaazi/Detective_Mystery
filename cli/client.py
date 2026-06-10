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

            if not message:

                break

            print(
                "\n" + message
            )

        except:

            break


def send():

    while True:

        try:

            msg = input("> ")

            if msg.lower() == "exit":

                client.send(
                    "exit".encode()
                )

                print(
                    "Keluar dari permainan..."
                )

                try:

                    client.shutdown(
                        socket.SHUT_RDWR
                    )

                except:

                    pass

                client.close()

                break

            client.send(
                msg.encode()
            )

        except KeyboardInterrupt:

            print(
                "\nKeluar dari permainan..."
            )

            try:

                client.shutdown(
                    socket.SHUT_RDWR
                )

            except:

                pass

            client.close()

            break


receiver = threading.Thread(
    target=receive
)

receiver.start()

send()

receiver.join()