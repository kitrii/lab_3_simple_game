from tkinter import *

root = Tk()
label = Label(width=20, text="Крестики-нолики", font=("Arial", 20, "bold"))
label.grid(row=0, column=0, columnspan=3)
label_info = Label(width=60, text="Первый ход принадлежит X", font=("Arial", 18, "bold"))
label_info.grid(row=4, column=0, columnspan=3)


state = 'x'
moves_x = []
moves_o = []
enabled_steps = list(range(9))
wins_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

buttons = [Button(width=8, height=5, font=("Arial", 40, "bold"), command=lambda x=i: push(x)) for i in range(9)]
raw = 1
col = 0
for i in range(9):
    if col == 3:
        col = 0
        raw += 1
    buttons[i].grid(padx=0, pady=0, row=raw, column=col)
    col += 1


def check_win(list_of_moves, state_player):
    win = []
    for combination in wins_combinations:
        for elem in combination:
            if elem in list_of_moves:
                win.append(True)
            else:
                win.append(False)
        if all(win):
            label_info['text'] = f"Игра окончена! {state_player} победил!!!"
            for i in enabled_steps:
                buttons[i].config(state="disabled")

        win.clear()


def end_game():
    if len(enabled_steps) == 0:
        label_info['text'] = "Игра окончена!"
        print("Вызывли конец")


def push(movement):
    global state
    if state == 'x':
        buttons[movement].config(text="x", state="disabled")
        moves_x.append(movement)
        enabled_steps.remove(movement)
        label_info['text'] = "X успешно совершил ход!"
        end_game()
        check_win(moves_x, state)
        state = 'o'
    elif state == 'o':
        buttons[movement].config(text="o", state="disabled")
        moves_o.append(movement)
        enabled_steps.remove(movement)
        label_info['text'] = "0 успешно совершил ход!"
        end_game()
        check_win(moves_o, state)
        state = 'x'


root.mainloop()
