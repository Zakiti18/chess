# chess.py
# Phillip Ball
# 5/26/2018
# This program lets the two users play chess.

##############################################################################
# imports the turtle and random modules
import turtle
import random
##############################################################################
# sets up the screen where you play
canvas = turtle.Screen()
canvas.bgcolor("#4d0000")
canvas.screensize(500, 500)
canvas.setup(width=502, height=502, startx=0, starty=0)
canvas.title("Chess")
##############################################################################
# sets up the turtle that makes the chessboard
board = turtle.Turtle()
board.speed(0)
##############################################################################
# makes the chessboard
# makes a function that creates the rows that start with a light tile
def l_chessboard(board):
    for i in range(4):
        board.color("sandybrown")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(21)
        board.color("saddlebrown")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(21)
# makes a function that creates the rows that start with a dark tile
def d_chessboard(board):
    for i in range(4):
        board.color("saddlebrown")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(21)
        board.color("sandybrown")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(21)
# 1st row
board.penup()
board.setposition(-110, 110)
board.forward(21)
board.pendown()
l_chessboard(board)
# 2nd row
board.penup()
board.setposition(-110, 89)
board.forward(21)
board.pendown()
d_chessboard(board)
# 3rd row
board.penup()
board.setposition(-110, 68)
board.forward(21)
board.pendown()
l_chessboard(board)
# 4th row
board.penup()
board.setposition(-110, 47)
board.forward(21)
board.pendown()
d_chessboard(board)
# 5th row
board.penup()
board.setposition(-110, 26)
board.forward(21)
board.pendown()
l_chessboard(board)
# 6th row
board.penup()
board.setposition(-110, 5)
board.forward(21)
board.pendown()
d_chessboard(board)
# 7th row
board.penup()
board.setposition(-110, -16)
board.forward(21)
board.pendown()
l_chessboard(board)
# 8th row
board.penup()
board.setposition(-110, -37)
board.forward(21)
board.pendown()
d_chessboard(board)
##############################################################################
# labels the grid of play
board.penup()
board.setposition(-83, 115)
board.color("white")
board.write("A")
board.forward(21)
board.write("B")
board.forward(21)
board.write("C")
board.forward(21)
board.write("D")
board.forward(21)
board.write("E")
board.forward(21)
board.write("F")
board.forward(21)
board.write("G")
board.forward(21)
board.write("H")
board.setposition(-100, -55)
board.setheading(90)
board.write("8")
board.forward(21)
board.write("7")
board.forward(21)
board.write("6")
board.forward(21)
board.write("5")
board.forward(21)
board.write("4")
board.forward(21)
board.write("3")
board.forward(21)
board.write("2")
board.forward(21)
board.write("1")
##############################################################################
# shows the types of pieces by color for player
# player pawn color
board.setposition(-66, -100)
board.color("aqua")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.right(180)
board.color("white")
board.forward(15)
board.write("P")
board.forward(10)
board.write("a")
board.forward(10)
board.write("w")
board.forward(10)
board.write("n")
# player rook color
board.setposition(-45, -100)
board.color("steelblue")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.right(180)
board.color("white")
board.forward(15)
board.write("R")
board.forward(10)
board.write("o")
board.forward(10)
board.write("o")
board.forward(10)
board.write("k")
# player knight color
board.setposition(-24, -100)
board.color("teal")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.right(180)
board.color("white")
board.forward(15)
board.write("K")
board.forward(10)
board.write("n")
board.forward(10)
board.write("i")
board.forward(10)
board.write("g")
board.forward(10)
board.write("h")
board.forward(10)
board.write("t")
# player bishop color
board.setposition(-3, -100)
board.color("slateblue")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.right(180)
board.color("white")
board.forward(15)
board.write("B")
board.forward(10)
board.write("i")
board.forward(10)
board.write("s")
board.forward(10)
board.write("h")
board.forward(10)
board.write("o")
board.forward(10)
board.write("p")
# player queen color
board.setposition(18, -100)
board.color("lightblue")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.right(180)
board.color("white")
board.forward(15)
board.write("Q")
board.forward(10)
board.write("u")
board.forward(10)
board.write("e")
board.forward(10)
board.write("e")
board.forward(10)
board.write("n")
# player king color
board.setposition(39, -100)
board.color("blue")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.right(180)
board.color("white")
board.forward(15)
board.write("K")
board.forward(10)
board.write("i")
board.forward(10)
board.write("n")
board.forward(10)
board.write("g")
##############################################################################
# shows the types of pieces by color for opponent
# opponent pawn color
board.setposition(-66, 150)
board.color("coral")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.color("white")
board.forward(15)
board.write("n")
board.forward(10)
board.write("w")
board.forward(10)
board.write("a")
board.forward(10)
board.write("P")
# opponent rook color
board.setposition(-45, 150)
board.color("firebrick")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.color("white")
board.forward(15)
board.write("k")
board.forward(10)
board.write("o")
board.forward(10)
board.write("o")
board.forward(10)
board.write("R")
# opponent knight color
board.setposition(-24, 150)
board.color("lightcoral")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.color("white")
board.forward(15)
board.write("t")
board.forward(10)
board.write("h")
board.forward(10)
board.write("g")
board.forward(10)
board.write("i")
board.forward(10)
board.write("n")
board.forward(10)
board.write("K")
# opponent bishop color
board.setposition(-3, 150)
board.color("crimson")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.color("white")
board.forward(15)
board.write("p")
board.forward(10)
board.write("o")
board.forward(10)
board.write("h")
board.forward(10)
board.write("s")
board.forward(10)
board.write("i")
board.forward(10)
board.write("B")
# opponent queen color
board.setposition(18, 150)
board.color("#ff4d4d")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.color("white")
board.forward(15)
board.write("n")
board.forward(10)
board.write("e")
board.forward(10)
board.write("e")
board.forward(10)
board.write("u")
board.forward(10)
board.write("Q")
# opponent king color
board.setposition(39, 150)
board.color("red")
board.setheading(90)
board.begin_fill()
for i in range(4):
    board.forward(15)
    board.right(90)
board.end_fill()
board.color("white")
board.forward(15)
board.write("g")
board.forward(10)
board.write("n")
board.forward(10)
board.write("i")
board.forward(10)
board.write("K")
##############################################################################
# shows the possible movements of each piece
# pawn rules
board.setposition(-245, 190)
board.setheading(0)
board.color("white")
board.write("Pawn.")
board.setposition(-245, 180)
board.write("The pawn moves one space")
board.setposition(-245, 170)
board.write("forward and can attack the")
board.setposition(-245, 160)
board.write("two forward diagonals.")
# rook rules
board.setposition(-245, 140)
board.write("Rook.")
board.setposition(-245, 130)
board.write("The rook can move left,")
board.setposition(-245, 120)
board.write("right, up and down")
board.setposition(-245, 110)
board.write("as far as you want.")
# knight rules
board.setposition(-245, 90)
board.write("Knight.")
board.setposition(-245, 80)
board.write("The knight moves in an L")
board.setposition(-245, 70)
board.write("shape, two in one of")
board.setposition(-245, 60)
board.write("the four directions, then")
board.setposition(-245, 50)
board.write("one to the left or right.")
board.setposition(-245, 40)
board.write("The only piece that can")
board.setposition(-245, 30)
board.write("move through others")
# bishop rules
board.setposition(-245, 10)
board.write("Bishop.")
board.setposition(-245, 0)
board.write("The bishop moves")
board.setposition(-245, -10)
board.write("diagonally as far")
board.setposition(-245, -20)
board.write("as you want.")
# queen rules
board.setposition(-245, -40)
board.write("Queen.")
board.setposition(-245, -50)
board.write("The queen can move up,")
board.setposition(-245, -60)
board.write("down, left, right, or")
board.setposition(-245, -70)
board.write("diagonally as far as")
board.setposition(-245, -80)
board.write("you want.")
# king rules
board.setposition(-245, -100)
board.write("King.")
board.setposition(-245, -110)
board.write("The king can move")
board.setposition(-245, -120)
board.write("one space in any")
board.setposition(-245, -130)
board.write("direction.")
board.setposition(-245, -140)
board.write("Be very careful with this")
board.setposition(-245, -150)
board.write("piece because if it is")
board.setposition(-245, -160)
board.write("taken, you lose.")
##############################################################################
# taken pieces piles
# red's side
# makes a function that creates the rows that start with a dark tile
def d_taken_blue(board):
    for i in range(4):
        board.color("red")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
        board.color("#ff4d4d")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
# makes a function that creates the rows that start with a light tile
def l_taken_blue(board):
    for i in range(4):
        board.color("#ff4d4d")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
        board.color("red")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
# makes row 1
board.setposition(150, 200)
board.setheading(270)
d_taken_blue(board)
# makes row 2
board.setposition(170, 200)
l_taken_blue(board)
##############################################################################
# blue's side
# makes a function that creates the rows that start with a dark tile
def d_taken_red(board):
    for i in range(4):
        board.color("blue")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
        board.color("lightblue")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
# makes a function that creates the rows that start with a light tile
def l_taken_red(board):
    for i in range(4):
        board.color("lightblue")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
        board.color("blue")
        board.begin_fill()
        for i in range(4):
            board.forward(20)
            board.right(90)
        board.end_fill()
        board.forward(20)
# makes row 1
board.setposition(130, -200)
board.setheading(90)
d_taken_red(board)
# makes row 2
board.setposition(150, -200)
l_taken_red(board)
##############################################################################
# hides the turtle that sets up the board
board.hideturtle()
#board.setposition(140, 73)
#board.shape("triangle")
#board.color("black")
#board.setheading(270)
##############################################################################
# sets up the player's pieces
# player pawn 1
p1 = turtle.Turtle()
p1.penup()
p1.shape("triangle")
p1.color("aqua")
p1.setheading(90)
p1.setposition(-79, -29)
# player pawn 2
p2 = turtle.Turtle()
p2.penup()
p2.shape("triangle")
p2.color("aqua")
p2.setheading(90)
p2.setposition(-58, -29)
# player pawn 3
p3 = turtle.Turtle()
p3.penup()
p3.shape("triangle")
p3.color("aqua")
p3.setheading(90)
p3.setposition(-37, -29)
# player pawn 4
p4 = turtle.Turtle()
p4.penup()
p4.shape("triangle")
p4.color("aqua")
p4.setheading(90)
p4.setposition(-16, -29)
# player pawn 5
p5 = turtle.Turtle()
p5.penup()
p5.shape("triangle")
p5.color("aqua")
p5.setheading(90)
p5.setposition(5, -29)
# player pawn 6
p6 = turtle.Turtle()
p6.penup()
p6.shape("triangle")
p6.color("aqua")
p6.setheading(90)
p6.setposition(26, -29)
# player pawn 7
p7 = turtle.Turtle()
p7.penup()
p7.shape("triangle")
p7.color("aqua")
p7.setheading(90)
p7.setposition(47, -29)
# player pawn 8
p8 = turtle.Turtle()
p8.penup()
p8.shape("triangle")
p8.color("aqua")
p8.setheading(90)
p8.setposition(68, -29)
# player rook 1
r1 = turtle.Turtle()
r1.penup()
r1.shape("triangle")
r1.color("steelblue")
r1.setheading(90)
r1.setposition(-79, -50)
# player rook 2
r2 = turtle.Turtle()
r2.penup()
r2.shape("triangle")
r2.color("steelblue")
r2.setheading(90)
r2.setposition(68, -50)
# player knight 1
h1 = turtle.Turtle()
h1.penup()
h1.shape("triangle")
h1.color("teal")
h1.setheading(90)
h1.setposition(-58, -50)
# player knight 2
h2 = turtle.Turtle()
h2.penup()
h2.shape("triangle")
h2.color("teal")
h2.setheading(90)
h2.setposition(47, -50)
# player bishop 1
b1 = turtle.Turtle()
b1.penup()
b1.shape("triangle")
b1.color("slateblue")
b1.setheading(90)
b1.setposition(-37, -50)
# player bishop 2
b2 = turtle.Turtle()
b2.penup()
b2.shape("triangle")
b2.color("slateblue")
b2.setheading(90)
b2.setposition(26, -50)
# player queen
q1 = turtle.Turtle()
q1.penup()
q1.shape("triangle")
q1.color("lightblue")
q1.setheading(90)
q1.setposition(5, -50)
# player king
k1 = turtle.Turtle()
k1.penup()
k1.shape("triangle")
k1.color("blue")
k1.setheading(90)
k1.setposition(-16, -50)
# makes a list with all the player pieces
player_pieces = [p1, p2, p3, p4, p5, p6, p7, p8, r1, r2, h1, h2, b1, b2, q1, k1]
player_pieces_full = ["pawn1", "pawn2", "pawn3", "pawn4", "pawn5", "pawn6", "pawn7", "pawn8", "rook1", "rook2", "knight1", "knight2", "bishop1", "bishop2", "queen1", "king1"]
##############################################################################
# sets up the opponent's pieces
# opponent pawn 1
p9 = turtle.Turtle()
p9.penup()
p9.shape("triangle")
p9.color("coral")
p9.setheading(270)
p9.setposition(-79, 82)
# opponent pawn 2
p10 = turtle.Turtle()
p10.penup()
p10.shape("triangle")
p10.color("coral")
p10.setheading(270)
p10.setposition(-58, 82)
# opponent pawn 3
p11 = turtle.Turtle()
p11.penup()
p11.shape("triangle")
p11.color("coral")
p11.setheading(270)
p11.setposition(-37, 82)
# opponent pawn 4
p12 = turtle.Turtle()
p12.penup()
p12.shape("triangle")
p12.color("coral")
p12.setheading(270)
p12.setposition(-16, 82)
# opponent pawn 5
p13 = turtle.Turtle()
p13.penup()
p13.shape("triangle")
p13.color("coral")
p13.setheading(270)
p13.setposition(5, 82)
# opponent pawn 6
p14 = turtle.Turtle()
p14.penup()
p14.shape("triangle")
p14.color("coral")
p14.setheading(270)
p14.setposition(26, 82)
# opponent pawn 7
p15 = turtle.Turtle()
p15.penup()
p15.shape("triangle")
p15.color("coral")
p15.setheading(270)
p15.setposition(47, 82)
# opponent pawn 8
p16 = turtle.Turtle()
p16.penup()
p16.shape("triangle")
p16.color("coral")
p16.setheading(270)
p16.setposition(68, 82)
# opponent rook 1
r3 = turtle.Turtle()
r3.penup()
r3.shape("triangle")
r3.color("firebrick")
r3.setheading(270)
r3.setposition(-79, 103)
# opponent rook 2
r4 = turtle.Turtle()
r4.penup()
r4.shape("triangle")
r4.color("firebrick")
r4.setheading(270)
r4.setposition(68, 103)
# opponent knight 1
h3 = turtle.Turtle()
h3.penup()
h3.shape("triangle")
h3.color("lightcoral")
h3.setheading(270)
h3.setposition(-58, 103)
# opponent knight 2
h4 = turtle.Turtle()
h4.penup()
h4.shape("triangle")
h4.color("lightcoral")
h4.setheading(270)
h4.setposition(47, 103)
# opponent bishop 1
b3 = turtle.Turtle()
b3.penup()
b3.shape("triangle")
b3.color("crimson")
b3.setheading(270)
b3.setposition(-37, 103)
# opponent bishop 2
b4 = turtle.Turtle()
b4.penup()
b4.shape("triangle")
b4.color("crimson")
b4.setheading(270)
b4.setposition(26, 103)
# opponent queen
q2 = turtle.Turtle()
q2.penup()
q2.shape("triangle")
q2.color("#ff4d4d")
q2.setheading(270)
q2.setposition(5, 103)
# opponent king
k2 = turtle.Turtle()
k2.penup()
k2.shape("triangle")
k2.color("red")
k2.setheading(270)
k2.setposition(-16, 103)
# makes a list with all the enemy pieces
enemy_pieces = [p9, p10, p11, p12, p13, p14, p15, p16, r3, r4, h3, h4, b3, b4, q2, k2]
enemy_pieces_full = ["pawn9", "pawn10", "pawn11", "pawn12", "pawn13", "pawn14", "pawn15", "pawn16", "rook3", "rook4", "knight3", "knight4", "bishop3", "bishop4", "queen2", "king2"]
##############################################################################
# general use functions and the turn switch
# sets up the turn switch
turn = True
# moves enemy pieces to their death spots once they are hit
def enemy_death_spot(enemy):
    if enemy == p16:
        p16.setposition(140, -192)
        p16.setheading(90)
        enemy_pieces_full.remove("pawn16")
        enemy_pieces.remove(p16)
    elif enemy == p15:
        p15.setposition(160, -192)
        p15.setheading(90)
        enemy_pieces_full.remove("pawn15")
        enemy_pieces.remove(p15)
    elif enemy == p14:
        p14.setposition(140, -172)
        p14.setheading(90)
        enemy_pieces_full.remove("pawn14")
        enemy_pieces.remove(p14)
    elif enemy == p13:
        p13.setposition(160, -172)
        p13.setheading(90)
        enemy_pieces_full.remove("pawn13")
        enemy_pieces.remove(p13)
    elif enemy == p12:
        p12.setposition(140, -152)
        p12.setheading(90)
        enemy_pieces_full.remove("pawn12")
        enemy_pieces.remove(p12)
    elif enemy == p11:
        p11.setposition(160, -152)
        p11.setheading(90)
        enemy_pieces_full.remove("pawn11")
        enemy_pieces.remove(p11)
    elif enemy == p10:
        p10.setposition(140, -132)
        p10.setheading(90)
        enemy_pieces_full.remove("pawn10")
        enemy_pieces.remove(p10)
    elif enemy == p9:
        p9.setposition(160, -132)
        p9.setheading(90)
        enemy_pieces_full.remove("pawn9")
        enemy_pieces.remove(p9)
    elif enemy == r3:
        r3.setposition(140, -112)
        r3.setheading(90)
        enemy_pieces_full.remove("rook3")
        enemy_pieces.remove(r3)
    elif enemy == r4:
        r4.setposition(160, -112)
        r4.setheading(90)
        enemy_pieces_full.remove("rook4")
        enemy_pieces.remove(r4)
    elif enemy == h3:
        h3.setposition(140, -92)
        h3.setheading(90)
        enemy_pieces_full.remove("knight3")
        enemy_pieces.remove(h3)
    elif enemy == h4:
        h4.setposition(160, -92)
        h4.setheading(90)
        enemy_pieces_full.remove("knight4")
        enemy_pieces.remove(h4)
    elif enemy == b3:
        b3.setposition(140, -72)
        b3.setheading(90)
        enemy_pieces_full.remove("bishop3")
        enemy_pieces.remove(b3)
    elif enemy == b4:
        b4.setposition(160, -72)
        b4.setheading(90)
        enemy_pieces_full.remove("bishop4")
        enemy_pieces.remove(b4)
    elif enemy == q2:
        q2.setposition(140, -52)
        q2.setheading(90)
        enemy_pieces_full.remove("queen2")
        enemy_pieces.remove(q2)
    elif enemy == k2:
        k2.setposition(160, -52)
        k2.setheading(90)
        enemy_pieces_full.remove("king2")
        enemy_pieces.remove(k2)
# moves player pieces to their death spots once they are hit
def player_death_spot(player):
    if player == p8:
        p8.setposition(160, 193)
        p8.setheading(270)
        player_pieces_full.remove("pawn8")
        player_pieces.remove(p8)
    elif player == p7:
        p7.setposition(140, 193)
        p7.setheading(270)
        player_pieces_full.remove("pawn7")
        player_pieces.remove(p7)
        
    elif player == p6:
        p6.setposition(160, 173)
        p6.setheading(270)
        player_pieces_full.remove("pawn6")
        player_pieces.remove(p6)
    elif player == p5:
        p5.setposition(140, 173)
        p5.setheading(270)
        player_pieces_full.remove("pawn5")
        player_pieces.remove(p5)
    elif player == p4:
        p4.setposition(160, 153)
        p4.setheading(270)
        player_pieces_full.remove("pawn4")
        player_pieces.remove(p4)
    elif player == p3:
        p3.setposition(140, 153)
        p3.setheading(270)
        player_pieces_full.remove("pawn3")
        player_pieces.remove(p3)
    elif player == p2:
        p2.setposition(160, 133)
        p2.setheading(270)
        player_pieces_full.remove("pawn2")
        player_pieces.remove(p2)
    elif player == p1:
        p1.setposition(140, 133)
        p1.setheading(270)
        player_pieces_full.remove("pawn1")
        player_pieces.remove(p1)
    elif player == r1:
        r1.setposition(160, 113)
        r1.setheading(270)
        player_pieces_full.remove("rook1")
        player_pieces.remove(r1)
    elif player == r2:
        r2.setposition(140, 113)
        r2.setheading(270)
        player_pieces_full.remove("rook2")
        player_pieces.remove(r2)
    elif player == h1:
        h1.setposition(160, 93)
        h1.setheading(270)
        player_pieces_full.remove("knight1")
        player_pieces.remove(h1)
    elif player == h2:
        h2.setposition(140, 93)
        h2.setheading(270)
        player_pieces_full.remove("knight2")
        player_pieces.remove(h2)
    elif player == b1:
        b1.setposition(160, 73)
        b1.setheading(270)
        player_pieces_full.remove("bishop1")
        player_pieces.remove(b1)
    elif player == b2:
        b2.setposition(140, 73)
        b2.setheading(270)
        player_pieces_full.remove("bishop2")
        player_pieces.remove(b2)
    elif player == q1:
        q1.setposition(160, 53)
        q1.setheading(270)
        player_pieces_full.remove("queen1")
        player_pieces.remove(q1)
    elif player == k1:
        k1.setposition(140, 53)
        k1.setheading(270)
        player_pieces_full.remove("king1")
        player_pieces.remove(k1)
# checks if pieces collide
# checks if a player runs into an enemy
def check_for_enemy(player, enemy_pieces):
    for enemy in enemy_pieces:
        if player.distance(enemy) <= 7:
            enemy_death_spot(enemy)
# checks if an enemy runs into a player
def check_for_player(enemy, player_pieces):
    for player in player_pieces:
        if enemy.distance(player) <= 7:
            player_death_spot(player)
##############################################################################
# sets up variables for each spot on the board
# player facing spots
# row 1
A1 = -79, 97
B1 = -58, 97
C1 = -37, 97
D1 = -16, 97
E1 = 5, 97
F1 = 26, 97
G1 = 47, 97
H1 = 68, 97
# row 2
A2 = -79, 76
B2 = -58, 76
C2 = -37, 76
D2 = -16, 76
E2 = 5, 76
F2 = 26, 76
G2 = 47, 76
H2 = 68, 76
# row 3
A3 = -79, 55
B3 = -58, 55
C3 = -37, 55
D3 = -16, 55
E3 = 5, 55
F3 = 26, 55
G3 = 47, 55
H3 = 68, 55
# row 4
A4 = -79, 34
B4 = -58, 34
C4 = -37, 34
D4 = -16, 34
E4 = 5, 34
F4 = 26, 34
G4 = 47, 34
H4 = 68, 34
# row 5
A5 = -79, 13
B5 = -58, 13
C5 = -37, 13
D5 = -16, 13
E5 = 5, 13
F5 = 26, 13
G5 = 47, 13
H5 = 68, 13
# row 6
A6 = -79, -8
B6 = -58, -8
C6 = -37, -8
D6 = -16, -8
E6 = 5, -8
F6 = 26, -8
G6 = 47, -8
H6 = 68, -8
# row 7
A7 = -79, -29
B7 = -58, -29
C7 = -37, -29
D7 = -16, -29
E7 = 5, -29
F7 = 26, -29
G7 = 47, -29
H7 = 68, -29
# row 8
A8 = -79, -50
B8 = -58, -50
C8 = -37, -50
D8 = -16, -50
E8 = 5, -50
F8 = 26, -50
G8 = 47, -50
H8 = 68, -50
# puts all the spots in a list
all_player_spots = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6, G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]
all_player_spots_string = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]
# enemy facing spots
# row 1
A1 = -79, 103
B1 = -58, 103
C1 = -37, 103
D1 = -16, 103
E1 = 5, 103
F1 = 26, 103
G1 = 47, 103
H1 = 68, 103
# row 2
A2 = -79, 82
B2 = -58, 82
C2 = -37, 82
D2 = -16, 82
E2 = 5, 82
F2 = 26, 82
G2 = 47, 82
H2 = 68, 82
# row 3
A3 = -79, 61
B3 = -58, 61
C3 = -37, 61
D3 = -16, 61
E3 = 5, 61
F3 = 26, 61
G3 = 47, 61
H3 = 68, 61
# row 4
A4 = -79, 40
B4 = -58, 40
C4 = -37, 40
D4 = -16, 40
E4 = 5, 40
F4 = 26, 40
G4 = 47, 40
H4 = 68, 40
# row 5
A5 = -79, 19
B5 = -58, 19
C5 = -37, 19
D5 = -16, 19
E5 = 5, 19
F5 = 26, 19
G5 = 47, 19
H5 = 68, 19
# row 6
A6 = -79, -2
B6 = -58, -2
C6 = -37, -2
D6 = -16, -2
E6 = 5, -2
F6 = 26, -2
G6 = 47, -2
H6 = 68, -2
# row 7
A7 = -79, -23
B7 = -58, -23
C7 = -37, -23
D7 = -16, -23
E7 = 5, -23
F7 = 26, -23
G7 = 47, -23
H7 = 68, -23
# row 8
A8 = -79, -44
B8 = -58, -44
C8 = -37, -44
D8 = -16, -44
E8 = 5, -44
F8 = 26, -44
G8 = 47, -44
H8 = 68, -44
# puts all the spots in a list
all_enemy_spots = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6, G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]
all_enemy_spots_string = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]
##############################################################################
# the game
while True:
    if turn == True:
        if "king1" not in player_pieces_full:
            print("Red player wins!")
            canvas.bye()
        else: 
            print("Blue player")
            print("Here is the list of available pieces.")
            for piece in player_pieces_full:
                print(piece)
            chosen_piece = input("Please choose a piece to move (example: pawn1): ")
            if chosen_piece not in player_pieces_full:
                print("That piece has either been taken or isn't yours, please choose another piece")
            chosen_piece = player_pieces_full.index(chosen_piece)
            chosen_piece = player_pieces[chosen_piece]
            chosen_spot = input("Please choose where you would like to move (example: A1): ")
            if chosen_spot not in all_player_spots_string:
                print("Please choose a spot on the board")
            chosen_spot = all_player_spots_string.index(chosen_spot)
            chosen_spot = all_player_spots[chosen_spot]
            chosen_piece.setposition(chosen_spot)
            check_for_enemy(chosen_piece, enemy_pieces)
            turn = False
    elif turn == False:
        if "king2" not in enemy_pieces_full:
            print("Blue player wins!")
            canvas.bye()
        else: 
            print("Red player")
            print("Here is the list of available pieces.")
            for piece in enemy_pieces_full:
                print(piece)
            chosen_piece = input("Please choose a piece to move (example: pawn9): ")
            if chosen_piece not in enemy_pieces_full:
                print("That piece has either been taken or isn't yours, please choose another piece")
            chosen_piece = enemy_pieces_full.index(chosen_piece)
            chosen_piece = enemy_pieces[chosen_piece]
            chosen_spot = input("Please choose where you would like to move (example: A1): ")
            if chosen_spot not in all_enemy_spots_string:
                print("Please choose a spot on the board")
            chosen_spot = all_enemy_spots_string.index(chosen_spot)
            chosen_spot = all_enemy_spots[chosen_spot]
            chosen_piece.setposition(chosen_spot)
            check_for_player(chosen_piece, player_pieces)
            turn = True
##############################################################################