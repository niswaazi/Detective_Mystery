from cases import CASE
from locations import LOCATIONS

inventories = {}
scores = {}


def create_player(name):

    inventories[name] = []
    scores[name] = 0


def get_help():

    return """
===== COMMAND =====

help

map

go <lokasi>

notes

suspects

chat <pesan>

accuse <nama>

exit

Contoh:
go Laboratorium
accuse Andi
exit
"""


def get_map():

    text = "\n=== LOKASI ===\n"

    for loc in LOCATIONS:

        text += f"- {loc}\n"

    return text


def investigate(player, location):

    if location not in CASE["clues"]:

        return "Lokasi tidak ditemukan."

    clue = CASE["clues"][location]

    if clue not in inventories[player]:

        inventories[player].append(clue)
        scores[player] += 10

    return clue


def get_notes(player):

    if len(inventories[player]) == 0:

        return "Belum ada petunjuk."

    text = "\n=== PETUNJUK ===\n"

    for clue in inventories[player]:

        text += f"- {clue}\n"

    return text


def get_suspects():

    text = "\n=== TERSANGKA ===\n"

    for name, shirt in CASE["suspects"].items():

        text += f"{name} : {shirt}\n"

    return text


def accuse(player, suspect):

    if suspect == CASE["criminal"]:

        return (
            True,
            f"""
KASUS TERPECAHKAN

Detektif : {player}

Pelaku : {CASE['criminal']}
Senjata : {CASE['weapon']}
Lokasi : {CASE['location']}

Skor : {scores[player]}
"""
        )

    scores[player] -= 20

    return False, "Tuduhan salah! -20 poin."