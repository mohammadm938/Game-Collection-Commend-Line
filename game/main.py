from colorama import Fore
import os

print(Fore.LIGHTBLUE_EX+"************************** خوش امدید **************************" +Fore.BLACK)
print("\n\n")

print("سنگ کاعذ قیچی[1]")
print("[2]بازی حدس عدد (کامپیوتر حدس میزند)")
print("[3]بازی حدس عدد (شما حدس میزنید)")

try:
    chooseGame=int(input("عدد بازی خود را انتخاب کنید : "))
except:
    print(Fore.RED+"فقط عدد وارد کنید")
    chooseGame=int(input("عدد بازی خود را انتخاب کنید : "))

if chooseGame==1:
    os.system('clear')
    os.system("python3 Rock-Paper-Scissors.py")
elif chooseGame==2:
    os.system('clear')
    os.system("python3 Game-guessing-number-by-computer.py")
elif chooseGame==3:
    os.system('clear')
    os.system("python3 Game-guessing-number.py")
    