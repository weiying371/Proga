import turtle
from Board import Board
from Cross_Zero import *

window = turtle.Screen()

board = Board()
board.show()

game_state = {"turn": "X", "cells": [None] * 9}


def check_winner():
    win_cel = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_cel:
        if game_state["cells"][a] == game_state["cells"][b] == game_state["cells"][c] and game_state["cells"][a] is not None:
            return game_state["cells"][a]

    if None not in game_state["cells"]:
        return "Нічия"

    return None


def play(x, y):
    col = (150 + x) // 100
    row = (150 - y) // 100

    if 0 <= col < 3 and 0 <= row < 3:
        idx = int(row * 3 + col)

        if game_state["cells"][idx] is None:
            cx = -100 + col * 100
            cy = 100 - row * 100

            if game_state["turn"] == "X":
                piece = Cross("blue")
                piece.set_position(cx, cy)
                piece.show()
                game_state["cells"][idx] = "X"
                game_state["turn"] = "O"
            else:
                piece = Zero("red")
                piece.set_position(cx, cy)
                piece.show()
                game_state["cells"][idx] = "O"
                game_state["turn"] = "X"

            winner = check_winner()
            if winner:
                game_state["active"] = False
                announce_winner(winner)

def announce_winner(winner):
    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, -180)
    if winner == "Нічия":
        announcer.write("Нічия!", align="center", font=("Arial", 20, "bold"))
    else:
        announcer.write(f"Переміг гравець {winner}!", align="center", font=("Arial", 20, "bold"))

if __name__ == '__main__':

    turtle.onscreenclick(play)
    turtle.listen()
    turtle.done()
