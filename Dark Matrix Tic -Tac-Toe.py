from tkinter import *

# this code is for Window Setup
root = Tk()
root.title("Dark Matrix Tic Tac Toe")
root.geometry("420x560")
root.configure(bg="#071A12")
root.resizable(False, False)

# About Game State
current_player = "X"
board = [""] * 9

# Game Title Label 
title_label = Label(
    root,
    text="Dark Matrix TIC TAC TOE",
    font=("Courier", 18, "bold"),
    bg="#071A12",
    fg="#00FF41"
)
title_label.pack(pady=(18, 0))
#  For Status Label
status = Label(
    root,text="Player X's Turn",
    font=("Courier", 14, "bold"),
    bg="#071A12",
    fg="gold"
)
status.pack(pady=(6, 10))

# For Game board frame 
game_frame = Frame(root, bg="#071A12")
game_frame.pack()

buttons = []

# Function for Win / Draw Check 
def check_winner():
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a], (a, b, c)
    return None, None

# Function for highlighting  Winning Cells 
def highlight_winner(winning_cells):
    for idx in winning_cells:
        buttons[idx].config(bg="#1A4D33", fg="#FFD700")

# Function for click on cells for play
def click(position):
    global current_player

    if board[position] != "":
        return

    board[position] = current_player

    # Color X as cyan, O as red

    color = "#00FFFF" if current_player == "X" else "#FF4444"
    buttons[position].config(text=current_player, fg=color, state=DISABLED, disabledforeground=color)

    winner, winning_cells = check_winner()

    if winner:
        highlight_winner(winning_cells)
        status.config(text=f"🎉  Player {winner}  Wins!", fg="#00FF41")
        for btn in buttons:
            btn.config(state=DISABLED)
        restart_btn.config(state=NORMAL)
        return

    if "" not in board:
        status.config(text="It's a Draw!", fg="orange")
        restart_btn.config(state=NORMAL)
        return

    current_player = "O" if current_player == "X" else "X"
    player_color = "gold"
    status.config(text=f"Player {current_player}'s Turn", fg=player_color)

#  Restart / Reset function
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    status.config(text="Player X's Turn", fg="gold")
    for btn in buttons:
        btn.config(
            text="",
            state=NORMAL,
            bg="#0D2B1D",
            fg="#00FF41"
        )
    restart_btn.config(state=DISABLED)

# Build Buttons 
for i in range(9):
    btn = Button(
        game_frame,
        text="",
        width=5,
        height=2,
        font=("Courier", 28, "bold"),
        bg="#0D2B1D",
        fg="#00FF41",
        activebackground="#1A4D33",
        activeforeground="#00FF41",
        relief="ridge",
        bd=3,
        cursor="hand2",
        command=lambda i=i: click(i)
    )
    btn.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )
    buttons.append(btn)

# ─── Score Tracker ──────────────────────────────────────────────
score = {"X": 0, "O": 0, "Draw": 0}

score_frame = Frame(root, bg="#071A12")
score_frame.pack(pady=14)

score_x_label = Label(score_frame, text="X: 0", font=("Courier", 12, "bold"),
                       bg="#071A12", fg="#00FFFF", width=8)
score_x_label.grid(row=0, column=0, padx=10)

score_draw_label = Label(score_frame, text="Draw: 0", font=("Courier", 12, "bold"),
                          bg="#071A12", fg="orange", width=10)
score_draw_label.grid(row=0, column=1, padx=10)

score_o_label = Label(score_frame, text="O: 0", font=("Courier", 12, "bold"),
                       bg="#071A12", fg="#FF4444", width=8)
score_o_label.grid(row=0, column=2, padx=10)

# this function Update Score After Each Game 
def click(position):
    global current_player

    if board[position] != "":
        return

    board[position] = current_player
    color = "#00FFFF" if current_player == "X" else "#FF4444"
    buttons[position].config(text=current_player, fg=color, state=DISABLED, disabledforeground=color)

    winner, winning_cells = check_winner()

    if winner:
        highlight_winner(winning_cells)
        status.config(text=f"🎉  Player {winner}  Wins!", fg="#00FF41")
        for btn in buttons:
            btn.config(state=DISABLED)
        score[winner] += 1
        update_score()
        restart_btn.config(state=NORMAL)
        return

    if "" not in board:
        status.config(text="It's a Draw!", fg="orange")
        score["Draw"] += 1
        update_score()
        restart_btn.config(state=NORMAL)
        return

    current_player = "O" if current_player == "X" else "X"
    status.config(text=f"Player {current_player}'s Turn", fg="gold")

def update_score():
    score_x_label.config(text=f"X: {score['X']}")
    score_o_label.config(text=f"O: {score['O']}")
    score_draw_label.config(text=f"Draw: {score['Draw']}")

#  Restart Button
restart_btn=Button(
    root,
    text="Restart Game",
    font=("Courier", 12, "bold"),
    bg="#0D2B1D",
    fg="gold",
    activebackground="#1A4D33",
    activeforeground="gold",
    relief="ridge",
    bd=3,
    cursor="hand2",
    state=DISABLED,
    command=reset_game
    )
restart_btn.pack(pady=(0, 18))

root.mainloop()