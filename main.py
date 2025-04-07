import random


class Mancala_Board:
    def __init__(self, mancala):
        if mancala is not None:
            self.mancala = mancala[:]
        else:
            self.mancala = [0 for _ in range(14)]
            for i in range(0, 6):
                self.mancala[i] = 4
            for i in range(7, 13):
                self.mancala[i] = 4

    def player_move(self, i):
        j = i
        repeat_turn = False
        add = self.mancala[j]
        self.mancala[j] = 0
        if i > 6:
            stones = add
            while stones > 0:
                i += 1
                i %= 14
                if i == 6:
                    continue
                self.mancala[i] += 1
                stones -= 1
            if (
                i > 6
                and self.mancala[i] == 1
                and i != 13
                and self.mancala[5 - (i - 7)] != 0
            ):
                self.mancala[13] += 1 + self.mancala[5 - (i - 7)]
                self.mancala[i] = 0
                self.mancala[5 - (i - 7)] = 0
            if i == 13:
                repeat_turn = True
        else:
            stones = add
            while stones > 0:
                i += 1
                i %= 14
                if i == 13:
                    continue
                self.mancala[i] += 1
                stones -= 1
            if i < 6 and self.mancala[i] == 1 and i != 6 and self.mancala[-i + 12] != 0:
                self.mancala[6] += 1 + self.mancala[-i + 12]
                self.mancala[i] = 0
                self.mancala[-i + 12] = 0
            if i == 6:
                repeat_turn = True
        return repeat_turn

    def isEnd(self):
        if sum(self.mancala[0:6]) == 0:
            self.mancala[13] += sum(self.mancala[7:13])
            for i in range(14):
                if i != 13 and i != 6:
                    self.mancala[i] = 0
            return True
        elif sum(self.mancala[7:13]) == 0:
            self.mancala[6] += sum(self.mancala[0:6])
            for i in range(14):
                if i != 13 and i != 6:
                    self.mancala[i] = 0
            return True
        return False

    def print_mancala(self):
        for i in range(12, 6, -1):
            print("  ", self.mancala[i], "   ", end="")
        print(
            "\n",
            self.mancala[13],
            "                                           ",
            self.mancala[6],
        )
        for i in range(0, 6, 1):
            print("  ", self.mancala[i], "   ", end="")
        print()

    def husVal(self):
        if self.isEnd():
            if self.mancala[13] > self.mancala[6]:
                return 100
            elif self.mancala[13] == self.mancala[6]:
                return 0
            else:
                return -100
        else:
            # Heuristic: Difference in stores + seeds in pits + potential captures
            player1_store = self.mancala[13]
            player2_store = self.mancala[6]
            player1_pits = sum(self.mancala[7:13])
            player2_pits = sum(self.mancala[0:6])
            return (player1_store - player2_store) + (player1_pits - player2_pits) * 0.5


def alphabeta(mancala, depth, alpha, beta, MinorMax):
    if depth == 0 or mancala.isEnd():
        return mancala.husVal(), -1
    if MinorMax:
        v = -1000000
        player_move = -1
        for i in range(7, 13):
            if mancala.mancala[i] == 0:
                continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv, _ = alphabeta(a, depth - 1, alpha, beta, minormax)
            if v < newv:
                player_move = i
                v = newv
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v, player_move
    else:
        v = 1000000
        player_move = -1
        for i in range(0, 6):
            if mancala.mancala[i] == 0:
                continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv, _ = alphabeta(a, depth - 1, alpha, beta, not minormax)
            if v > newv:
                player_move = i
                v = newv
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v, player_move


def player_player():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("PLAYER 1 TURN >>> "))
            if h < 7 or h > 12 or j.mancala[h] == 0:
                print("Invalid position. Choose another.")
                continue
            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            h = int(input("PLAYER 2 TURN >>> "))
            if h > 5 or j.mancala[h] == 0:
                print("Invalid position. Choose another.")
                continue
            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
    print_winner(j)


def player_aibot():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("YOUR TURN >>> "))
            if h > 5 or j.mancala[h] == 0:
                print("Invalid position. Choose another.")
                continue
            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("AI-BOT TURN >>> ", end="")
            _, k = alphabeta(j, 10, -100000, 100000, True)
            print(k)
            t = j.player_move(k)
            j.print_mancala()
            if not t:
                break
    print_winner(j)


def ai_vs_ai():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            print("AI-BOT 1 TURN >>> ", end="")
            # AI-BOT 1 uses depth 8
            _, k = alphabeta(j, 6, -100000, 100000, True)
            print(k)
            t = j.player_move(k)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("AI-BOT 2 TURN >>> ", end="")
            # AI-BOT 2 uses depth 6 and adds randomness
            _, k = alphabeta(j, 8, -100000, 100000, False)
            if random.random() < 0.1:  # 10% chance to pick a random valid move
                valid_moves = [i for i in range(0, 6) if j.mancala[i] > 0]
                if valid_moves:
                    k = random.choice(valid_moves)
            print(k)
            t = j.player_move(k)
            j.print_mancala()
            if not t:
                break
    print_winner(j)


def print_winner(j):
    if j.mancala[13] > j.mancala[6]:
        print("PLAYER 1 / AI-BOT 1 WINS")
    elif j.mancala[13] < j.mancala[6]:
        print("PLAYER 2 / AI-BOT 2 WINS")
    else:
        print("IT'S A DRAW")
    print("GAME ENDED")
    j.print_mancala()


# --- Main Menu ---

print("\n:::: MANCALA BOARD GAME ::::")
print("!!! Welcome to Mancala Gameplay !!!")

while True:
    print("\nChoose your Gameplay Type")
    print("(1) Player-1 vs Player-2")
    print("(2) Player vs AI-Bot")
    print("(3) AI-Bot vs AI-Bot")
    try:
        game_type = int(input(">>> "))
        if game_type == 1:
            player_player()
            break
        elif game_type == 2:
            player_aibot()
            break
        elif game_type == 3:
            ai_vs_ai()
            break
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Enter a valid number.")
