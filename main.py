import pyautogui as p
import subprocess as sp

from time import sleep as s

print("Start _________________________________________")

class BAviso:

    account = "avisoo"
    aber_check = "./aberavel/check_title.png"
    picYoutube = "picYoutube.png"
    heart_first_png = "heart_first_png.png"
    squerYoutube = "squerYoutube.png"
    perform = "perform.png"
    check = "check.png"
    my_pay = "my_pay.png"
    no_balance = "no_balance.png"
    no_access = "no_access.png"
    no_task = "no_task.png"
    continue_more = True
    check_title = "./aberavel/check_title.png" #"check_title.png" # "./aberavel/check_title.png" #

    def __init__(self, pics):
        # self.account = "aberavel"
        self.account = "avisoo"

        # self.aber_check = "./aberavel/check_title.png"
        self.aber_check = "check_title.png"

        self.perform = "perform.png"


        self.check = "check.png"

        self.my_pay = "my_pay.png"
        self.no_balance = "no_balance.png"
        self.no_access = "no_access.png"
        self.no_task = "no_task.png"

        self.pics = pics
        self.continue_more = True


    def search_all_pic_screen(self, pic):
        return [match for match in p.locateAllOnScreen(pic)]

    def moveToLink(self, pic, shift_x=0, shift_y=0, time=0.3):
        matchs = self.search_all_pic_screen(pic)
        if matchs !=[]:
            p.moveTo(matchs[0][0]+ matchs[0][2]+shift_x, matchs[0][1]+shift_y, time)

    def wait_pic(self, pic, time=1):
        while self.search_all_pic_screen(pic) == []:
            if self.search_all_pic_screen(self.my_pay) != [] or self.search_all_pic_screen(
                    self.no_balance) != [] or self.search_all_pic_screen(self.no_access) != []:
                s(1.5)
                self.continue_more = False
                break

            print(f"waiting {pic}")
            s(time)


    def find_kudos_in_comment(self, pics):
            for  pic in pics:
                matchs = self.search_all_pic_screen(pic)
                print(matchs)
                s(1)
                if matchs != []:
                    self.moveToLink(pic, 10, 13)
                    p.click()
                    self.wait_pic(self.perform)
                    print("fined perform? go to click")
                    self.moveToLink(self.perform, -5, 3)
                    p.click()
                    p.move(15, 55, 0.3)
                    # no_access

                    print("continue_more ", self.continue_more)
                    if self.continue_more:
                        self.wait_pic(self.check_title)
                        p.hotkey("ctrl", "w")
                        self.wait_pic(self.check)
                        self.moveToLink(self.check, -10, 5)
                        p.click()
                        self.wait_pic(self.my_pay)
                    self.continue_more = True
                    p.hotkey("f5")
                    s(1)

            if self.search_all_pic_screen(self.no_task) != []:

                    p.moveTo(self.search_all_pic_screen(self.no_task)[0][0], self.search_all_pic_screen(self.no_task)[0][1])
                    p.click()
                    print("pause per 5 sec")
                    s(5)

                    p.hotkey("f5")
                    s(3)

    def goToURL(self, url="https://aviso.bz/work-youtube"):
        s(2)
        p.hotkey("ctrl", "l")
        s(1)
        p.hotkey("ctrl", "a")
        p.write(url, 1)
        p.hotkey("ENTER")
        s(3)

picYoutube = "picYoutube.png"
heart_first = "heart_first_png.png"
squerYoutube = "squerYoutube.png"
pics = [squerYoutube, heart_first, picYoutube]
go = BAviso(pics)

while True:

    go.find_kudos_in_comment(pics)
