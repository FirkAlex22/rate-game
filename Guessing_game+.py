# Импорт библиоткеки
from Crypt_num_for_Guessing_game import crypt, decrypt
import random
from colorama import init, Back, Fore, Style
init()
opt_file = open("opt_file.txt", mode = "r+", encoding="latin_1")
# Очки
points = 5000
points_s_opt_file = opt_file.read()
points = points_s_opt_file
points = decrypt(points)

# points = opt_file
skip = True
def rate_chek():
    global rate, client_num, points, rate
    random_num = random.randint(1,10)
# Ставка и игра
    print(Fore.GREEN)
    print(Back.WHITE)
    try:
        print("Enter your bid no more than "+ str(points), "and no less than 0:")
        rate = input(">")
    # Много или мало ставки
        if int(rate) < 0 or int(rate) > int(points):
            print("Enough!")
    # Правильная ставка
        elif int(rate) > 0 and int(rate) <= int(points):
            print("Now enter the number from 1 to 10:")
    # Ввод пользовательского числа
        client_num = int(input(">"))
        try:
            if client_num > 0 and (client_num)<=10 and client_num != 0:
                if client_num == random_num:
                    points = int(points) - int(rate)
                    points = int(points) + (int(rate)* 2)
                    print("You have won a double bet, The number was "+ str(random_num))
                elif client_num != random_num:
                    points = int(points) - int(rate)
                    print("You lost the bet, your balance: "+ str(points))
                    print("number was "+ str(random_num))
            else:
                print("Enter normale number!")
        except ValueError:
            opt_file.seek(0)
            points = crypt(points)
            opt_file.write(str(points))
            opt_file.close()
            print("Enter normale number!")
    except ValueError:
        opt_file.seek(0)
        points = crypt(points)
        opt_file.write(str(points))
        opt_file.close()
        print("Enter normale number!")



# Цикличность игры
while skip:
    random_num = random.randint(1,10)
    rate_chek()
    print("Your balance: "+ str(points))
    skip = input("To continue type \"/skip\", if not, then \"/exit\": \n>")
    if skip == "/skip" or skip == "skip":
        rate_chek()
    elif skip != "skip" or (skip == "exit" or skip == "/exit"):
        opt_file.seek(0)
        points = crypt(points)
        opt_file.write(str(points))
        opt_file.close()
        skip = False
# Проверка баланса
while skip:
    if points <= 0:
        print("Your balance is less than 0")
        opt_file.seek(0)
        points = crypt(points)
        opt_file.write(str(points))
        opt_file.close()
        skip = False
        input()
