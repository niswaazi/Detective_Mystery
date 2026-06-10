from flask import Flask, render_template, request

app = Flask(__name__)

CASE = {
    "criminal": "Andi",
    "weapon": "Pisau",
    "location": "Laboratorium"
}

CLUES = [
    "Sidik jari Andi ditemukan di meja korban.",
    "Surat ancaman ditulis oleh Andi.",
    "Mobil Andi terlihat meninggalkan kampus pukul 22.05.",
    "Saksi melihat seseorang berbaju merah keluar dari laboratorium."
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template(
        "game.html",
        clues=CLUES
    )

@app.route("/accuse", methods=["POST"])
def accuse():

    suspect = request.form["suspect"]

    if suspect == CASE["criminal"]:

        result = "KASUS TERPECAHKAN!"

    else:

        result = "Tuduhan Salah!"

    return render_template(
        "result.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)