import random
import os
import time
from colorama import Fore, just_fix_windows_console

just_fix_windows_console()


def clear():
    os.system("cls")


def sleep(x):
    time.sleep(x)


clear()
print("=-=-=-=-=-=", Fore.GREEN,
      "WELCOME TO ROCK PAPER SCISSOR GAME", Fore.RESET, "=-=-=-=-=-=")
sleep(2)
clear()
while True:
    print(Fore.RED, "[+]", "CHOOSE:\n", Fore.YELLOW,
          "1] Rock \n 2] Paper \n 3] Scissor", Fore.CYAN)
    a = int(input("[+]>>>"))
    b = random.randint(1, 3)
    if a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1:
        print(Fore.RED, "YOU LOSE!")
    if a == 2 and b == 1 or a == 3 and b == 2 or a == 1 and b == 3:
        print(Fore.GREEN, "YOU WIN!")
    else:
        print(Fore.YELLOW, "NEXT MATCH")
    continue
