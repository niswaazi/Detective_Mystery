import socket
import threading

from game import *

HOST = "0.0.0.0"
PORT = 5001

clients = []
usernames = {}


def broadcast(message):

    for client in clients:

        try:

            client.send(
                message.encode()
            )

        except:

            pass


def handle(client):

    username = None

    while True:

        try:

            message = client.recv(
                1024
            ).decode()

            if not message:

                break

            if message.startswith("LOGIN:"):

                username = message.split(":")[1]

                usernames[client] = username

                create_player(username)

                client.send(
                    f"""
Selamat datang Detektif {username}

Ketik help untuk melihat command.
""".encode()
                )

                broadcast(
                    f"{username} bergabung ke permainan."
                )

                continue

            if message == "exit":

                broadcast(
                    f"{username} keluar dari permainan."
                )

                break

            if message == "help":

                client.send(
                    get_help().encode()
                )

                continue

            if message == "map":

                client.send(
                    get_map().encode()
                )

                continue

            if message.startswith("go "):

                location = message[3:]

                clue = investigate(
                    username,
                    location
                )

                client.send(
                    clue.encode()
                )

                continue

            if message == "notes":

                client.send(
                    get_notes(username).encode()
                )

                continue

            if message == "suspects":

                client.send(
                    get_suspects().encode()
                )

                continue

            if message.startswith("chat "):

                text = message[5:]

                broadcast(
                    f"[{username}] {text}"
                )

                continue

            if message.startswith("accuse "):

                suspect = message[7:]

                correct, result = accuse(
                    username,
                    suspect
                )

                if correct:

                    broadcast(
                        result
                    )

                else:

                    client.send(
                        result.encode()
                    )

                continue

        except:

            break

    if client in clients:

        clients.remove(client)

    if client in usernames:

        del usernames[client]

    client.close()


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(
    (HOST, PORT)
)

server.listen()

print(
    f"Server berjalan pada port {PORT}"
)

while True:

    client, addr = server.accept()

    clients.append(client)

    print(
        f"Client terhubung {addr}"
    )

    threading.Thread(
        target=handle,
        args=(client,)
    ).start()