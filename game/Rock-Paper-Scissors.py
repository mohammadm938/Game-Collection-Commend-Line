from colorama import Fore
import random
import os


class colors:
    bg = '\x1b[0m'
    starter = Fore.LIGHTBLUE_EX
    winner = Fore.LIGHTGREEN_EX
    loser = Fore.LIGHTRED_EX
    equal = Fore.LIGHTBLACK_EX

    

def welocme(name, playerScore, computerScore):
    print(colors.starter+"************************** خوش امدید %s **************************" %
          name + "\n\n"+colors.bg)
    print("از بین گزینه های زیر انتخاب خود را وارد کنید ." +
          "\n"+"کاغذ[1]"+"\n"+"سنگ[2]"+"\n"+"قیچی[3]"+"\n")
    print(colors.winner+"امتیاز شما : "+str(playerScore)+colors.bg)
    print(colors.loser+"امتیاز کامپیوتر : "+str(computerScore)+colors.bg)


def computerChoose():
    number = random.randrange(1, 4)
    if number == 1:
        number = "کاغذ"
    elif number == 2:
        number = "سنگ"
    elif number == 3:
        number = "قیچی"
    return number


def playerChoose(number):
    if number == 1:
        number = "کاغذ"
    elif number == 2:
        number = "سنگ"
    elif number == 3:
        number = "قیچی"
    return number


def cheakWinner(computer, player):
    # E=> Equal
    # P => Player Win
    # C => Computer Win
    if computer == player:
        return[computer, player, "E"]
    elif computer == "کاغذ" and player == "سنگ":
        return[computer, player, "C"]
    elif player == "کاغذ" and computer == "سنگ":
        return[computer, player, "P"]
    elif computer == "سنگ" and player == "قیچی":
        return[computer, player, "C"]
    elif player == "سنگ" and computer == "قیچی":
        return[computer, player, "P"]
    elif computer == "قیچی" and player == "کاغذ":
        return[computer, player, "C"]
    elif player == "قیچی" and computer == "کاغذ":
        return[computer, player, "P"]

def game(playerChooseNumber):
    resultWinner = cheakWinner(
        computerChoose(), playerChoose(playerChooseNumber))
    return resultWinner


def getPoint(winner, computerScore, playerScore):
    if winner == "E":
        return[computerScore, playerScore, "اع مساوی شدید که ", colors.equal]
    elif winner == "C":
        return[computerScore+10, playerScore, "کامپیوتر برد", colors.loser]
    elif winner == "P":
        return[computerScore, playerScore+10, "شما بردید", colors.winner]



def cheakWinnerAllGame(playerScore, computerScore,equal=""):
    if playerScore > computerScore:
        return ["شما برنده شدید با اختلاف امتیازه : ", colors.winner,playerScore-computerScore]
    elif playerScore < computerScore:
        return ["کامپیوتر برنده شد با اختلاف امتیازه : ", colors.loser,computerScore-playerScore]
    elif playerScore == computerScore:
        return ["بازی مساوی شد", colors.equal,equal]


# Game start
playOrLeave = input("آیا مایل به شروع بازی هستیذ؟(yes / no)")
if playOrLeave == "yes":
    stop = False
    print("به بازی سنگ/کاغذ/قیچی خوش آمدید")
    name = input("لطفا نام خود را وارد کنید: ")
    computerScore = 0
    playerScore = 0
    welocme(name, playerScore, computerScore)

    while stop == False:
        try:
            playerChooseNumber = int(input("شماره انتخاب خود را وارد کنید : "))
            if playerChooseNumber != 1 and playerChooseNumber != 2 and playerChooseNumber != 3:
                print("عددی بین 1 تا 3 انتخاب کنید")
                playerChooseNumber = int(
                    input("شماره انتخاب خود را وارد کنید : "))
        except:
            print("لطفا فقط عدد را وارد کنید و از وارد کردن رشته متنی خودداری کنید")
            playerChooseNumber = int(input("شماره انتخاب خود را وارد کنید : "))

        resultWinner = game(playerChooseNumber)
        computerEndChoose = resultWinner[0]
        playerEndChoose = resultWinner[1]
        winner = resultWinner[2]

        resultPoint = getPoint(winner, computerScore, playerScore)
        computerScore = resultPoint[0]
        playerScore = resultPoint[1]
        messageWinner = resultPoint[2]
        colorToShow = resultPoint[3]

        print("\n"+colorToShow+messageWinner+colors.bg)
        print("انتخاب کامپیوتر : "+computerEndChoose)
        print("انتخاب شما : "+playerEndChoose)
        print("امتیاز شما : "+str(playerScore))
        print("امتیاز کامپیوتر : "+str(computerScore))

        askToContinue = input("ایا میخواهید ادامه بدید ؟؟ (yes/no)")
        if askToContinue == "no":
            os.system('clear')
            result = cheakWinnerAllGame(playerScore, computerScore)
            message = result[0]
            color = result[1]
            scoreDifference=str(result[2])
            print(color+message+scoreDifference+colors.bg)
            stop = True
        else:
            os.system('clear')
            welocme(name, playerScore, computerScore)
            game(playerChooseNumber)

else:
    print("منتظر شما میمانیم")