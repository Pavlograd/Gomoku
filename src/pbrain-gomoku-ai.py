#!/usr/bin/python3
##
# EPITECH PROJECT, 2020
# 305construction
# File description:
# 305construction
##
# functions and variables for pipe AI and functions that communicate with manager through pipes
# don't modify this file

import sys
from random import *

DEBUG      = False
ABOUT_FUNC = True
DEBUG_EVAL = True

original_stdout = sys.stdout

# information about a game - you should use these variables
"""the board size"""
width = None
"""time for one turn in milliseconds"""
info_timeout_turn = 30000
"""total time for a game"""
info_timeout_match = 1000000000
"""left time for a game"""
info_time_left = 1000000000
"""maximum memory in bytes, zero if unlimited"""
info_max_memory = 0
"""0: human opponent, 1: AI opponent, 2: tournament, 3: network tournament"""
info_game_type = 1
"""0: five or more stones win, 1: exactly five stones win"""
info_exact5 = 0
"""0: gomoku, 1: renju"""
info_renju = 0
"""0: single game, 1: continuous"""
info_continuous = 0
"""return from brain_turn when terminateAI > 0"""
terminateAI = None
"""tick count at the beginning of turn"""
start_time = None
"""folder for persistent files"""
dataFolder = ""

info_rule = 0

board = []

info_board_1 = []
info_board_2 = []

event1, event2 = None, None

def printBoard():
    global board

    for line in board:
        print(line)
    #print(board)

def pipeOut(what):
    """write a line to sys.stdout"""
    #with open('filename.txt', 'w') as f:
    #    sys.stdout = f # Change the standard output to the file we created.
    #    print('This message will be written to a file.')
    #    sys.stdout = original_stdout # Reset the standard output to its original value
    #ret = len(what)
    print(what)
    sys.stdout.flush()

def throwERROR():
    pipeOut("ERROR")
    exit(0)

def setInfosTurn(x, y, player, opponent):
    global info_board_1
    global info_board_2
    global board
    global width
    turn = 0
    stop = 0
    possibilities = 0
    actual_x = x
    actual_y = y
    info_board = []

    info_board.append(x)
    info_board.append(y)

    while turn < 8:
        if turn == 0:
            while stop != 4:
                if actual_x - 1 >= 0: 
                    if board[actual_x - 1][actual_y] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_x = actual_x - 1
                    else:
                        stop = 4
                else:
                    stop = 4
        elif turn == 1:
            while stop != 4:
                if actual_y + 1 <= width - 1 and actual_x > 0: 
                    if board[actual_x - 1][actual_y + 1] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_x = actual_x - 1
                        actual_y = actual_y + 1
                    else:
                        stop = 4
                else:
                    stop = 4
        elif turn == 2:
            while stop != 4:
                if actual_y + 1 <= width - 1: 
                    if board[actual_x][actual_y + 1] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_y = actual_y + 1
                    else:
                        stop = 4
                else:
                    stop = 4
        elif turn == 3:
            while stop != 4:
                if actual_y + 1 <= width - 1 and actual_x + 1 <= width - 1: 
                    if board[actual_x + 1][actual_y + 1] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_y = actual_y + 1
                        actual_x = actual_x + 1
                    else:
                        stop = 4
                else:
                    stop = 4
        elif turn == 4:
            while stop != 4:
                if actual_x + 1 <= width - 1: 
                    if board[actual_x + 1][actual_y] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_x = actual_x + 1
                    else:
                        stop = 4
                else:
                    stop = 4
        elif turn == 5:
            while stop != 4:
                if actual_x + 1 <= width - 1 and actual_y - 1 >= 0: 
                    if board[actual_x + 1][actual_y - 1] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_x = actual_x + 1
                        actual_y = actual_y - 1
                    else:
                        stop = 4
                else:
                    stop = 4
        elif turn == 6:
            while stop != 4:
                if actual_y - 1 >= 0: 
                    if board[actual_x][actual_y - 1] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_y = actual_y - 1
                    else:
                        stop = 4
                else:
                    stop = 4
        elif turn == 7:
            while stop != 4:
                if actual_y - 1 >= 0 and actual_x - 1 >= 0: 
                    if board[actual_x - 1][actual_y - 1] != opponent:
                        possibilities= possibilities + 1
                        stop = stop + 1
                        actual_y = actual_y - 1
                        actual_x = actual_x - 1
                    else:
                        stop = 4
                else:
                    stop = 4
        info_board.append(possibilities)
        stop = 0
        possibilities = 0
        actual_x = x
        actual_y = y
        turn = turn + 1
    
    info_board.append(0)
    info_board.append(0)
    info_board.append(0)
    info_board.append(0)
    info_board.append(0)
    info_board.append(0)
    info_board.append(0)
    info_board.append(0)

    if player == 1:
        info_board_1.append(info_board)
    else:
        info_board_2.append(info_board)
    setOtherInfosTurn(x, y, player, opponent)
    return

def info_command(line):
    if len(line) != 3:
        return
    if line[1] == "max_memory":
        global info_max_memory
        info_max_memory = int(line[2])
    elif line[1] == "timeout_turn":
        global info_timeout_turn
        info_timeout_turn = int(line[2])
    elif line[1] == "timeout_match":
        global info_timeout_match
        info_timeout_match = int(line[2])
    elif line[1] == "time_left":
        global info_time_left
        info_time_left = int(line[2])
    elif line[1] == "game_type":
        global info_game_type
        info_game_type = int(line[2])
    elif line[1] == "rule":
        global info_rule
        info_rule = int(line[2])
    elif line[1] == "folder":
        global dataFolder
        dataFolder = line[2]

def start_command(line):
    global width
    global board

    if len(line) == 2:
        width = int(line[1])
        if width < 5 or width > 20:
            pipeOut("ERROR")
            exit(0)
        board = [[0]*width for i in range(width)]
    pipeOut('OK')

def random_attack():
    global board
    global width
    x = 0
    y = 0

    while 1:
        x = randint(0, width - 1)
        y = randint(0, width - 1)
        if board[x][y] == 0:
           break
    return x,y

def begin_command():
    ai_response()

def setOtherInfosTurnSecond(player):
    global info_board_1
    global info_board_2

    tmp_board = []

    if player == 1:
        tmp_board = info_board_1
    else:
        tmp_board = info_board_2

    for pawn in tmp_board:
        pawn[10] = 0
        pawn[11] = 0
        pawn[12] = 0
        pawn[13] = 0
        pawn[14] = 0
        pawn[15] = 0
        pawn[16] = 0
        pawn[17] = 0

    for pawn2 in tmp_board:
        x = pawn2[0]
        y = pawn2[1]
        for pawn in tmp_board:
            if pawn[0] - x == 0 and pawn[1] - y != 0:
                if pawn[1] - y > 0 and pawn[1] - y <= pawn[8]:
                    pawn[16] = pawn[16] + 1
                elif pawn[1] - y < 0 and pawn[1] - y >= -1 * pawn[4]:
                    pawn[12] = pawn[12] + 1
            elif pawn[1] - y == 0 and pawn[0] - x != 0:
                if pawn[0] - x > 0 and pawn[0] - x <= pawn[2]:
                    pawn[10] = pawn[10] + 1
                elif pawn[0] - x < 0 and pawn[0] - x >= -1 * pawn[6]:
                    pawn[14] = pawn[14] + 1
            elif pawn[1] - y == pawn[0] - x and pawn[1] - y != 0 and abs(pawn[1] - y) <= 4:
                if pawn[1] - y > 0 and pawn[9] - abs(pawn[1] - y) >= 0:
                    pawn[17] = pawn[17] + 1
                elif pawn[5] - abs(pawn[1] - y) >= 0:
                    pawn[13] = pawn[13] + 1
            elif abs(pawn[1] - y) == abs(pawn[0] - x) and pawn[1] - y != 0 and abs(pawn[1] - y) <= 4:
                if pawn[1] - y > 0 and pawn[7] - abs(pawn[1] - y) >= 0:
                    pawn[15] = pawn[15] + 1
                elif pawn[3] - abs(pawn[1] - y) >= 0:
                    pawn[11] = pawn[11] + 1

def setOtherInfosTurn(x, y, player, opponent):
    global info_board_1
    global info_board_2

    tmp_board = []

    if player == 1:
        tmp_board = info_board_2
    else:
        tmp_board = info_board_1

    for pawn in tmp_board:
        if pawn[0] - x == 0:
            if pawn[1] - y > 0 and pawn[1] - y <= pawn[8]:
                pawn[8] = pawn[8] - (abs(abs(pawn[1] - y) - pawn[8]) + 1)
            elif pawn[1] - y < 0 and pawn[1] - y >= -1 * pawn[4]:
                pawn[4] = pawn[4] - (abs(abs(pawn[1] - y) - pawn[4]) + 1)
        elif pawn[1] - y == 0:
            if pawn[0] - x > 0 and pawn[0] - x <= pawn[2]:
                pawn[2] = pawn[2] - (abs(abs(pawn[0] - x) - pawn[2]) + 1)
            elif pawn[0] - x < 0 and pawn[0] - x >= -1 * pawn[6]:
                pawn[6] = pawn[6] - (abs(abs(pawn[0] - x) - pawn[6]) + 1)
        elif pawn[1] - y == pawn[0] - x and pawn[1] - y != 0 and abs(pawn[1] - y) <= 4:
            if pawn[1] - y > 0:
                pawn[9] = min(pawn[9], abs(pawn[1] - y) - 1)
            else:
                pawn[5] = min(pawn[5], abs(pawn[1] - y) - 1)
        elif abs(pawn[1] - y) == abs(pawn[0] - x) and pawn[1] - y != 0 and abs(pawn[1] - y) <= 4:
            if pawn[1] - y > 0:
                pawn[7] = min(pawn[7], abs(pawn[1] - y) - 1)
            else:
                pawn[3] = min(pawn[3], abs(pawn[1] - y) - 1)
    #print(player, tmp_board)
    for pawn in tmp_board:
        i = 2
        while i < 10:
            if pawn[i] < 0:
                pawn[i] = 0
            i = i + 1
    setOtherInfosTurnSecond(player)
    setOtherInfosTurnSecond(opponent)

def playPawn(pawn, sizeLine, firstLine, firstNbrPawn):
    global board
    global width

    x = pawn[0]
    y = pawn[1]

    #print(sizeLine, firstLine)

    if firstLine == 2:
        if pawn[firstLine] - pawn[firstNbrPawn] >= 1:
            if sizeLine == 4:
                if x < width + 1 and board[x + 1][y] == 0:
                    x = x + 1
                elif x < width + 2 and board[x + 2][y] == 0:
                    x = x + 2
                elif x < width + 3 and board[x + 3][y] == 0:
                    x = x + 3
                elif x < width + 4 and board[x + 4][y] == 0:
                    x = x + 4
                else:
                    while x >= 0 and board[x][y] != 0:
                        x = x - 1
            else:
                while x >= 0 and board[x][y] != 0:
                    x = x - 1
        else:
            while x < width and board[x][y] != 0:
                x = x + 1
    elif firstLine == 3:
        if pawn[firstLine] - pawn[firstNbrPawn] >= 1:
            while y < width and x >= 0 and board[x][y] != 0:
                y = y + 1
                x = x - 1
        else:
            while x < width and y >= 0 and board[x][y] != 0:
                y = y - 1
                x = x + 1
    elif firstLine == 5:
        if pawn[firstLine] - pawn[firstNbrPawn] >= 1:
            while y < width and x < width and board[x][y] != 0:
                y = y + 1
                x = x + 1
        else:
            while y >= 0 and x >= 0 and board[x][y] != 0:
                y = y - 1
                x = x - 1
    elif firstLine == 4:
        if pawn[firstLine] - pawn[firstNbrPawn] >= 1:
            while y < width and board[x][y] != 0:
                y = y + 1
        else:
            while y >= 0 and board[x][y] != 0:
                y = y - 1
    else:
        return random_attack()
    if x >= width or y >= width or x < 0 or y < 0:
        return random_attack()
    #print("Played: ", x, y)
    return x,y

def ai_response():
    global board
    global info_board_1
    global info_board_2

    x = 0
    y = 0
    size = 0
    size_enemy = 0
    x_enemy = 0
    y_enemy = 0
    x, y = random_attack()

    if len(info_board_2) > 0:
        sizeLine = 5
        played = False
        while sizeLine >= 1:
            for pawn in info_board_2:
                firstLine = 2
                firstNbrPawn = 10
                while firstLine <= 5:
                    if 1 + pawn[firstNbrPawn] + pawn[firstNbrPawn + 4] == sizeLine and (pawn[firstLine] - pawn[firstNbrPawn] >= 1 or pawn[firstLine + 4] - pawn[firstNbrPawn + 4] >= 1):
                        x_enemy, y_enemy = playPawn(pawn, sizeLine, firstLine, firstNbrPawn)
                        played = True
                        break
                    firstLine = firstLine + 1
                    firstNbrPawn = firstNbrPawn + 1
                if played:
                    break
            if played:
                size_enemy = sizeLine
                break
            sizeLine = sizeLine - 1
    if len(info_board_1) > 0:
        sizeLine = 5
        played = False
        while sizeLine >= 1:
            for pawn in info_board_1:
                firstLine = 2
                firstNbrPawn = 10
                while firstLine <= 5:
                    if 1 + pawn[firstNbrPawn] + pawn[firstNbrPawn + 4] == sizeLine and (pawn[firstLine] - pawn[firstNbrPawn] >= 1 or pawn[firstLine + 4] - pawn[firstNbrPawn + 4] >= 1):
                        x, y = playPawn(pawn, sizeLine, firstLine, firstNbrPawn)
                        played = True
                        break
                    firstLine = firstLine + 1
                    firstNbrPawn = firstNbrPawn + 1
                if played:
                    break
            if played:
                size = sizeLine
                break
            sizeLine = sizeLine - 1
    
    if size_enemy > 0 and size_enemy > size:
        x = x_enemy
        y = y_enemy

    board[x][y] = 1
    #printBoard()
    setInfosTurn(x, y, 1, 2)
    pipeOut(str(x) + ',' + str(y))

def turn_command(line):
    global board

    line[1] = line[1].split(",")

    if len(line[1]) != 2:
        throwERROR()
    
    board[int(line[1][0])][int(line[1][1])] = 2
    setInfosTurn(int(line[1][0]), int(line[1][1]), 2, 1)

    #printBoard()
    #if int(line[1][2]) == 2:
    #    setInfosTurn(int(line[1][0]), int(line[1][1]), 2, 1)
    #else:
    #    setInfosTurn(int(line[1][0]), int(line[1][1]), 1, 2)
    ai_response()

def about_command():
    pipeOut('name="pbrain-gomoku-ai", version="1.0", author="Maurin", country="FRANCE"')

def board_command(line):
    global board

    while 1:
        line = input()
        line = line.split()

        if line[0] == "DONE":
            ai_response()
            return
        else:
            line[0] = line[0].split(",")
            board[int(line[0][0])][int(line[0][1])] = int(line[0][2])
            if int(line[0][2]) == 2:
                setInfosTurn(int(line[0][0]), int(line[0][1]), 2, 1)
            else:
                setInfosTurn(int(line[0][0]), int(line[0][1]), 1, 2)

def main():
    """main function for AI console application"""
    while 1:
        try:
            line = input().split()
            if line[0] == "END":
                return(0)
            elif line[0] == "START":
                start_command(line)
            elif line[0] == "INFO":
                info_command(line)
            elif line[0] == "BEGIN":
                if len(line) != 1:
                    throwERROR()
                begin_command()
            elif line[0] == "TURN":
                turn_command(line)
            elif line[0] == "ABOUT":
                about_command()
            elif line[0] == "BOARD":
                board_command(line)
            else:
                pipeOut(line)
        except EOFError as e:
            return(0)
        except:
            pipeOut("ERROR")
            return(0)
    return (0)

try:
    if __name__ == "__main__":
        main()
except EOFError as e:
    pass
except:
    pipeOut("ERROR")
    pass
