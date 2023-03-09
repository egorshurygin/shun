from sqlite3 import *
from random import *
import os
from CodeFromDisplay import way

genered_CardID = set()
print(way)


def get_balance_by_telegram_id(tg_id):
    conn = connect(way)
    cur = conn.cursor()
    cur.execute(f"SELECT BALANCE FROM Bottle WHERE TELEGRAM_ID == {tg_id};")
    balance = cur.fetchone()[0]
    conn.commit()
    return balance


def make_new_line_in_database(tg_id):
    global genered_CardID
    conn = connect(way)
    cur = conn.cursor()
    new_CardID = list(set(i for i in range(100000, 1000000)) - genered_CardID)
    shuffle(new_CardID)
    new_CardID = new_CardID[0]
    print(new_CardID, tg_id)
    try:
        cur.execute(f"INSERT INTO Bottle (TELEGRAM_ID, CARD_ID) VALUES({tg_id}, {new_CardID});")
        genered_CardID.add(new_CardID)
    except IntegrityError:
        pass
    conn.commit()


def add_to_balance_in_database(tg_id, points):
    conn = connect(way)
    cur = conn.cursor()
    balance = get_balance_by_telegram_id(tg_id) + points
    cur.execute(f"UPDATE Bottle SET BALANCE = {balance} WHERE TELEGRAM_ID == {tg_id};")
    conn.commit()
