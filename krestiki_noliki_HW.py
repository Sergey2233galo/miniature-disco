def decoration_for_game(func):
    def wrapper():
        print("Привет! Это обычные крестики-нолики. "
              "Ходите по очереди выбирая от 1 до 9. "
              "Для выхода нажмите 'q'. "
              "Кто первый построит линию из 3х в ряд - тот выигрывает.")
        func()
        print("Спасибо за игру, надеюсь вы хорошо провели время.")
    return wrapper

changes = {1:'*',2:'*',3:'*',4:'*',5:'*',6:'*',7:'*',8:'*',9:'*'}

win_list = (
    (1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)
)

def desk():
    print(f'#  1  2  3')
    print(f'1  {changes[7]}  {changes[8]}  {changes[9]}')
    print(f'2  {changes[4]}  {changes[5]}  {changes[6]}')
    print(f'3  {changes[1]}  {changes[2]}  {changes[3]}')

@decoration_for_game
def the_game():
    count = 1
    numbers = []
    gamer = 'X'
    player_X = []
    player_O = []
    activ = True
    while activ:
        desk()
        a = input(f"Ход игрока {gamer}, выберите от 1 до 9, 'q' для выхода  ")
        if a == 'q':
            print("До свидания !")
            break
        elif a in list(map(str, range(1,10))):
            if a in numbers:
                print("Попробуй еще, это число уже было")
            else:
                numbers.append(a)
                if count == 9:
                    print("Конец. Это ничья.")
                    break
                if count % 2 == 1:
                    gamer = 'O'
                    changes[int(a)] = 'X'
                    player_X.append(int(a))
                    count += 1
                    for i in win_list:
                        if len(set(player_X).intersection(i)) == 3:
                            print("Игрок X победил")
                            activ = False
                        else:
                            continue
                elif count % 2 == 0:
                    gamer = 'X'
                    changes[int(a)] = 'O'
                    player_O.append(int(a))
                    count += 1
                    for i in win_list:
                        if len(set(player_O).intersection(i)) == 3:
                            print("Игрок O победил")
                            activ = False
                        else:
                            continue
        else:
            print("Пожалуйста выберите число от 1 до 9,'q' для выхода")
            continue

the_game()


