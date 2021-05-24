from colorama import Fore
import random
import os


class colors:
    bg = '\x1b[0m'
    starter = Fore.LIGHTBLUE_EX
    winner = Fore.LIGHTGREEN_EX
    loser = Fore.LIGHTRED_EX
    equal = Fore.LIGHTBLACK_EX

def computerChoose():
    answer = random.randint(1, 99)
    return answer

def cheakWinner(playerThink,answer,name):
    if playerThink == answer:
        return Fore.GREEN+"آفرین %s شما جواب را پیدا کردید" % name+Fore.BLACK
    else:
        return Fore.RED+"شما جواب را پیدا نکردید"

def welocme(name):
    return colors.starter+"************************** خوش امدید %s **************************" %name + "\n\n"+colors.bg

answer=computerChoose()
askNumbers = 0
name = str(input("لطفا نام خود را وارد کنید: "))
welocme=welocme(name)
os.system('clear')
print(welocme)

playerThink = int(input("عددی که حدس میزنید را وارد کنید : "))

while playerThink != answer:
    if askNumbers <= 12:
        if playerThink > answer:
            print(Fore.LIGHTRED_EX+"عددت بزرگتر از عددی هست که من انتخاب کردم"+Fore.BLACK)
            playerThink = int(input("دوباره حدس بزن : "))
            askNumbers += 1
        elif playerThink < answer:
            print(Fore.LIGHTCYAN_EX +
                  "عددت کوچکتر تر از عددی هست که من انتخاب کردم"+Fore.BLACK)
            playerThink = int(input("دوباره حدس بزن : "))
            askNumbers += 1
    else:
        break


messageWinner=cheakWinner(playerThink,answer,name)
print(messageWinner)
