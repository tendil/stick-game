#ВАРИАНТ ПЕРВЫЙ

from random import choice

print("* " * 8,'\nИгра в палочки!\n' + '* ' * 8, '\n\n')
wand = int(input("Введи количество палoчек для игры - "))
wand_amount = wand
print(f"* " * 10, f"\nНа столе {wand_amount} палочек\n" + "* " * 10)
game_continue = True
player_real = 0
bot_palyer = 0

def winMM(kol_p, name):
    global game_continue, player_real, bot_palyer, wand_amount
    if wand_amount <= 0:
        print(f'\nПобедил {name}!!')
        answer = input('Сыграем заново?: ').lower()
        game_continue = False
        if answer in ['да', 'давай', 'конечно', 'lf', 'y', 'yes']:
            wand_amount = wand
            player_real = 0
            bot_palyer = 0
            game_continue = True
    return game_continue

def player_choice():
    global wand_amount
    pl_choice = int(input(f"\nСколько возьмешь? - [1, 2, 3]\n"))
    print(f"Ты взял {pl_choice} палочек")
    wand_amount -= pl_choice
    print(f"Всего осталось {wand_amount} палочек")
    return pl_choice

def pc_player_chpice():
    global wand_amount
    pc_choice = choice([1, 2, 3])
    print(f"PC взял {pc_choice} палочек")
    wand_amount -= pc_choice
    print(f"Всего осталось {wand_amount} палочек")
    return pc_choice

while game_continue:
    player_ch = player_choice()
    player_real += player_ch
    print(f'У вас {player_real} палочек\n' + "-" * 25)
    winMM(wand_amount, 'Bot')

    pc_choice = pc_player_chpice()
    bot_palyer += pc_choice
    print(f"У PC {bot_palyer} палочек")
    winMM(wand_amount, 'Playerr')

#ВАРИАНТ ВТОРОЙ

# choice_wand = int(input("Введи колество стиков для игры - "))
# player = "Player 1"
#
# while choice_wand > 0:
#     choice = int(input(f"\nВсего осталось: {choice_wand}.\nСколько стиков возьмёшь? [1, 2, 3] - "))
#     if choice < 1 or choice > 3:
#         print(f"Ты взял {choice} стиков, а можно только 1, 2, 3")
#         continue
#
#     choice_wand -= choice
#     print(f"Стиков взято {choice}\n")
#
#     if choice_wand <= 0:
#         print(f"Стики закончились. {player} проиграл(")
#
#     player = "Player 1" if player == "Player 2" else "Player 2"











