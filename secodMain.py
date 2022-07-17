import pyautogui as p
import subprocess as sp

from time import sleep as s



account = "aberavel"
account = "avisoo"


aber_check = "./aberavel/check_title.png"
picYoutube = "picYoutube.png"
heart_first_png = "heart_first_png.png"
squerYoutube = "squerYoutube.png"

perform = "perform.png"

if account == "aberavel":
    check_title = aber_check
else:
    check_title = "check_title.png"

check = "check.png"

my_pay = "my_pay.png"
no_balance = "no_balance.png"
no_access = "no_access.png"
no_task = "no_task.png"

pics = [squerYoutube,  heart_first_png, picYoutube,]

def search_all_pic_screen(pic):
    return [match for match in p.locateAllOnScreen(pic)]

def moveToLink(pic, shift_x=0, shift_y=0, time=0.3):
    matchs = search_all_pic_screen(pic)
    if matchs !=[]:
        p.moveTo(matchs[0][0]+ matchs[0][2]+shift_x, matchs[0][1]+shift_y, time)

def wait_pic(pic, time=1):
    while search_all_pic_screen(pic) == []:
        if search_all_pic_screen(my_pay) != [] or search_all_pic_screen(no_balance) != [] or search_all_pic_screen(no_access) != []:
            s(1.5)
            break
        print(f"waiting {pic}")
        s(time)


def find_kudos_in_comment(pics, perform):
        for  pic in pics:
            matchs = search_all_pic_screen(pic)
            print(matchs)
            s(1)
            if matchs != []:
                moveToLink(pic, 10, 13)
                p.click()
                wait_pic(perform)
                print("fined perform? go to click")
                moveToLink(perform, -5, 3)
                p.click()
                p.move(15, 55, 0.3)
                wait_pic(check_title)
                p.hotkey("ctrl", "w")
                wait_pic(check)
                moveToLink(check, -10, 5)
                p.click()
                wait_pic(my_pay)
                p.hotkey("f5")
                s(1)

        if search_all_pic_screen(no_task) != []:

                p.moveTo(search_all_pic_screen(no_task)[0][0], search_all_pic_screen(no_task)[0][1])
                p.click()
                print("waiting 60 sec")
                s(60)
                p.hotkey("f5")
                s(3)

            # perform = [match for match in p.locateAllOnScreen("perform.png", confidence=0.8)]
            # p.moveTo(perform[0][0], perform[0][1])
            # p.click()
            # s(30)
            # # Waiting
            # check_title = [match for match in p.locateAllOnScreen("check_title.png", confidence=0.8)]
            # p.moveTo(check_title[0][0], check_title[0][1], 0.5)
            # p.hotkey("ctrl", "w")
            # s(1)
            # check = [match for match in p.locateAllOnScreen("check.png", confidence=0.8)]
            # p.moveTo(check[0][0]+25, check[0][1] +10, 0.5)
            #
            # s(1)
            # p.hotkey("f5")
            # s(3)


def goToURL(url="https://aviso.bz/work-youtube"):
    s(2)
    p.hotkey("ctrl", "l")
    s(1)
    p.hotkey("ctrl", "a")
    p.write(url, 1)
    p.hotkey("ENTER")
    s(3)

while True:
    find_kudos_in_comment(pics, perform)
