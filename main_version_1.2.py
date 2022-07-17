import pyautogui as p
import subprocess as sp

from time import sleep as s

print("Start _________________________________________")

class BAviso:
    browser = ""
    browser_ico = ""

    account = "avisoo"
    aber_check = "./aberavel/check_title.png"
    picYoutube = "picYoutube.png"
    heart_first_png = "heart_first_png.png"
    squerYoutube = "squerYoutube.png"
    perform = "perform.png"
    check = "check.png"
    my_pay = "my_pay.png"
    click_check_more = "click_check_more.png"
    no_balance = "no_balance.png"
    no_access = "no_access.png"
    no_task = "no_task.png"
    continue_more = True
    check_title = "" #"./aberavel/check_title.png" #"check_title.png" # "./aberavel/check_title.png" #

    def __init__(self, pics, browser, browser_ico, check_title):
        self.browser = browser
        self.browser_ico = browser_ico

        # self.account = "aberavel"
        self.click_check_more = "click_check_more.png"
        self.account = "avisoo"
        # self.aber_check = "./aberavel/check_title.png"
        self.aber_check = "check_title.png"
        self.perform = "perform.png"
        self.check_title = check_title
        self.check = "check.png"
        self.my_pay = "my_pay.png"
        self.no_balance = "no_balance.png"
        self.no_access = "no_access.png"
        self.no_task = "no_task.png"
        self.pics = pics
        self.continue_more = True

    def start_bot(self):
        self.moveToLink(self.browser_ico, 2)


    def search_all_pic_screen(self, pic):
        return [match for match in p.locateAllOnScreen(pic)]

    def moveToLink(self, pic, shift_x=0, shift_y=0, time=0.3):
        matchs = self.search_all_pic_screen(pic)
        if matchs !=[]:
            p.moveTo(matchs[0][0]+ matchs[0][2]+shift_x, matchs[0][1]+shift_y, time)
        else:
            print("element not defined")
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
                    s(0.2)
                    p.click()
                    s(0.1)
                    # p.click()
                    p.move(15, 55, 0.3)
                    # no_access

                    print("continue_more ", self.continue_more)
                    if self.continue_more:
                        self.wait_pic(self.check_title)
                        p.hotkey("ctrl", "w")
                        self.wait_pic(self.check)
                        self.moveToLink(self.check, -10, 5)
                        p.click()
                        p.move(10, -5)
                        while True:
                            if self.search_all_pic_screen(self.my_pay) != []:
                                break
                            if self.search_all_pic_screen(self.click_check_more) != []:
                                s(2)
                                self.moveToLink(self.check, - 10, 5)

                    self.continue_more = True
                    p.hotkey("f5")
                    s(1)
                    return False
            return True

            # if self.search_all_pic_screen(self.no_task) != []:
            #
            #         p.moveTo(self.search_all_pic_screen(self.no_task)[0][0], self.search_all_pic_screen(self.no_task)[0][1])
            #         p.click()
            #         print("pause per 5 sec")
            #         s(5)
            #
            #         p.hotkey("f5")
            #         s(3)

    def goToURL(self, url="https://aviso.bz/work-youtube"):
        s(2)
        p.hotkey("ctrl", "l")
        s(1)
        p.hotkey("ctrl", "a")
        p.write(url, 1)
        p.hotkey("ENTER")
        s(3)

    def f5(self, x=600, y=500, time=0.3):
        p.moveTo(x, y, time)
        p.hotkey("f5")

    def bot_minimize(self, time=1):
        print("browser", self.browser)
        self.moveToLink(self.browser, -110, 20, time)

picYoutube = "picYoutube.png"
heart_first = "heart_first_png.png"
squerYoutube = "squerYoutube.png"
pics = [squerYoutube, heart_first, picYoutube]

browser_chrome = "browser_chrome.png"
browser_chrome_ico = "browser_chrome_ico.png"
avisoooooo_check_title = "./aberavel/check_title.png"
avisoooooo = BAviso(pics, browser_chrome, browser_chrome_ico, avisoooooo_check_title)

browser_firefox = "browser_firefox.png"
browser_firefox_ico = "browser_firefox_ico.png"
firefo_check_title = "check_title_firefox.png"
firefo = BAviso(pics, browser_firefox, browser_firefox_ico, firefo_check_title)

browser_yandex_ico = "browser_yandex_ico.png"
avisoooo_check_title = "check_title.png"
browser_yandex ="browser_yandex.png"
avisoooo = BAviso(pics, browser_yandex, browser_yandex_ico, avisoooo_check_title)

# bots = [ firefo, avisoooo, avisoooooo, ]
# bots = [ firefo] # , avisoooo, avisoooooo, ]
#bots = [ avisoooo, avisoooooo, ]
bots = [ avisoooooo]

def go(bot):
    bot_count = 0
    # bot.start_bot()
    # s(0.2)
    # p.click()
    # s(1)
    while True:
        if bot.find_kudos_in_comment(pics):
            bot.f5()
            bot_count += 1
        if bot_count == 1:
            break
    # s(1)
    # bot.bot_minimize(time=1.5)
    # s(1)

    p.click()

    # bot end

while True:
    for bot in bots:
        print(bot.browser)
        go(bot)
