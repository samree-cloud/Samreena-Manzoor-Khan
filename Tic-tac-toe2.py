from tkinter import *

root = Tk()
root.title("Dark Matrix Tic Tac Toe")
root.geometry("400x500")
root.configure(bg="#071A12")


current_player = "X"
board = [""] * 9


status = Label(
    root,
    text="Player X Turn",
    font=("Arial", 16, "bold"),
    bg="#071A12",
    fg="gold"
)
status.pack(pady=10)


game_frame = Frame(root, bg="#071A12")
game_frame.pack()


buttons = []


def check_winner():

    winning_lines = [

        (0,1,2),
        (3,4,5),
        (6,7,8),

        (0,3,6),
        (1,4,7),
        (2,5,8),

        (0,4,8),
        (2,4,6)
    ]


    for a,b,c in winning_lines:

        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    return None



def click(position):

    global current_player


    if board[position] != "":
        return


    board[position] = current_player
    buttons[position]["text"] = current_player


    winner = check_winner()


    if winner:

        status.config(
            text=f"Player {winner} Wins!"
        )

        for btn in buttons:
            btn.config(state=DISABLED)

        return



    if "" not in board:

        status.config(text="Draw Game")

        return



    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"



    status.config(
        text=f"Player {current_player} Turn"
    )



for i in range(9):

    btn = Button(
        game_frame,
        text="",
        width=5,
        height=2,
        font=("Arial",24,"bold"),
        bg="#0D2B1D",
        fg="lime",
        activebackground="#1A4D33",
        relief="ridge",
        bd=3,
        command=lambda i=i: click(i)
    )


    btn.grid(
        row=i//3,
        column=i%3,
        padx=3,
        pady=3
    )


    buttons.append(btn)



root.mainloop()