from flask import Flask, render_template, request, jsonify
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "server"
        )
    )
)

from game import *
from cases import CASE
from locations import LOCATIONS

app = Flask(__name__)

chat_messages = []

players = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    return render_template(
        "game.html",
        locations=LOCATIONS
    )


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]

    if username not in players:

        create_player(username)
        players[username] = True

    return jsonify({"status": "ok"})


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    username = data["username"]
    message = data["message"]

    if message.strip():

        chat_messages.append(
            f"{username}: {message}"
        )

    return jsonify({"status": "ok"})


@app.route("/messages")
def messages():

    return jsonify(chat_messages)


@app.route("/investigate", methods=["POST"])
def investigate_location():

    data = request.get_json()

    username = data["username"]
    location = data["location"]

    if username not in players:

        create_player(username)
        players[username] = True

    clue = investigate(
        username,
        location
    )

    return jsonify({
        "clue": clue
    })


@app.route("/notes")
def notes():

    username = request.args.get(
        "username"
    )

    if username not in players:

        return jsonify({
            "notes": "Belum login."
        })

    return jsonify({
        "notes":
        get_notes(username)
    })


@app.route("/suspects")
def suspects():

    return jsonify(
        CASE["suspects"]
    )


@app.route("/score")
def score():

    username = request.args.get(
        "username"
    )

    if username not in scores:

        return jsonify({
            "score": 0
        })

    return jsonify({
        "score":
        scores[username]
    })


@app.route("/accuse", methods=["POST"])
def accuse_route():

    username = request.form["username"]
    suspect = request.form["suspect"]

    correct, result = accuse(
        username,
        suspect
    )

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )