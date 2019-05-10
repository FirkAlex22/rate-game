# Принцип таков, что прога считывает тхт файл его декодирует с помощью функции
#  потом работает с ним, в конце его опять шифрует, файл обнуляет и записывает
# Импорт библиоткеки
# Guessing-game+
# Chennel https://clck.ru/FvdFV
# Mail firkalex22l@gmail.com
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
#Cheat
def cheat_money():
    global points, opt_file, money, decrypt, crypt
    print(Fore.RED + "[cheat]" + Style.RESET_ALL + Fore.YELLOW + "how many it is necessary for you money?" + Style.RESET_ALL)
    opt_file = open("opt_file.txt", mode = "r+", encoding="latin_1")
    money = int(input("> "))
    points = int(points) + money
    opt_file.seek(0)
    points = crypt(points)
    opt_file.write(str(points))
    points = decrypt(points)
    return points
# Цвета
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
# points = opt_file
skip = True
# Main
def rate_chek():
    global rate, client_num, points, rate
    opt_file = open("opt_file.txt", mode = "r+", encoding="latin_1")
    random_num = random.randint(1,10)
# Ставка и игра
    # print(Fore.GREEN)
    # print(Back.WHITE)
    try:
        print(Fore.GREEN + "[!]" + Style.RESET_ALL + Fore.CYAN + "Enter your bid no more than " + str(points), "and no less than 0:" + Style.RESET_ALL)
        rate = input("> ")
    # Много или мало ставки
        if int(rate) < 0 or int(rate) > int(points):
            print(Fore.CYAN + "[!]" + Style.RESET_ALL + Fore.RED + "Enough!" + Style.RESET_ALL)
    # Правильная ставка
        elif int(rate) > 0 and int(rate) <= int(points):
            print(Fore.GREEN + "[!]" + Style.RESET_ALL + Fore.CYAN + "Now enter the number from 1 to 10:" + Style.RESET_ALL)
    # Ввод пользовательского числа
        client_num = int(input("> "))
        try:
            if client_num > 0 and (client_num) <= 10 and client_num != 0:
                if client_num == random_num:
                    points = int(points) - int(rate)
                    points = int(points) + (int(rate)* 2)
                    print(Fore.GREEN + "[+]" + Style.RESET_ALL + Fore.RED + "You have won a double bet!!!! The number was " + str(random_num) + Style.RESET_ALL)
                elif client_num != random_num:
                    points = int(points) - int(rate)
                    opt_file = open("opt_file.txt", mode = "r+", encoding="latin_1")
                    print(Fore.GREEN + "[-]" + Style.RESET_ALL + Fore.RED + "You lost the bet, your balance: " + str(points) + Style.RESET_ALL)
                    print(Fore.GREEN + "[!]" + Style.RESET_ALL + Fore.CYAN + "number was " + str(random_num) + Style.RESET_ALL)
            else:
                print(Fore.RED + "[!]" + Style.RESET_ALL + Fore.CYAN + "Enter normale number!" + Style.RESET_ALL)
        except ValueError:
            if rate == "//cheat_money":
                cheat_money()
            else:
                print("Enter normale number!")
    except ValueError:
        if rate == "//cheat_money":
            cheat_money()
        else:
            print("Enter normale number!")


# Цикличность игры
while skip:
    random_num = random.randint(1,10)
    rate_chek()
    print(Fore.GREEN + "[!]" + Style.RESET_ALL + Fore.CYAN +  "Your balance: " + str(points) + Style.RESET_ALL)
    print(Fore.GREEN + "[!]" + Style.RESET_ALL + Fore.YELLOW + "To continue press Enter, otherwise then \"/exit\":" + Style.RESET_ALL)
    skip = input("> ")
    if skip == "":
        rate_chek()
    elif skip == "//cheat_money":
        cheat_money()
    elif skip != "" or (skip == "exit" or skip == "/exit"):
        opt_file = open("opt_file.txt", mode = "r+", encoding="latin_1")
        opt_file.seek(0)
        points = crypt(points)
        opt_file.write(str(points))
        opt_file.close()
        skip = False
# Проверка баланса
while skip:
    if points <= 0:
        print(Fore.GREEN + "[!]" + Style.RESET_ALL + Fore.CYAN +  "Your balance is less than 0" + Style.RESET_ALL)
        opt_file = open("opt_file.txt", mode = "r+", encoding="latin_1")
        opt_file.seek(0)
        points = crypt(points)
        opt_file.write(str(points))
        opt_file.close()
        skip = False
        input()
