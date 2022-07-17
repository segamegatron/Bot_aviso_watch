import pyautogui as p
import subprocess as sp

from time import sleep as s

print("Start _________________________________________")

class BAviso:
    next_watch = 0
    name = ""
    browser = ""
    browser_ico = ""
    account_name = "account_name.png"
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
    x = [()]
    y = [()]
    def __init__(self, pics, browser, browser_ico, check_title, account_name):

        self.timer = "timer.png"
        self.count_miss = 0
        self.no_video = "no_video.png"
        self.end_movie = "end_movie.png"
        self.my_pay_from_youtube = "my_pay_from_youtube.png"
        self.order_not_found = "order_not_found.png"
        self.account_name = account_name
        self.browser = browser
        self.browser_ico = browser_ico

        self.click_check_more = "click_check_more.png"
        self.account = "avisoo"
        self.aber_check = "check_title.png"
        self.perform = "perform.png"
        self.youtube_ico = "youtube_ico.png"
        self.youtube_active_ico = "youtube_active_ico.png"
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

    def search_all_pic_screen(self, pic, confidence=0.9):
        return [match for match in p.locateAllOnScreen(pic, confidence=confidence)]

    def moveToLink(self, pic, shift_x=0, shift_y=0, time=0.3):
        matchs = self.search_all_pic_screen(pic, 0.9)
        if matchs !=[]:
            print("match from move to link ", matchs[0])
            p.moveTo(matchs[0][0]+ matchs[0][2]+shift_x, matchs[0][1]+shift_y, time)
        else:
            print("element not defined")

    def wait_pic(self, pic, waiting_time=0 ,time=1, count=1):
        while self.search_all_pic_screen(pic) == []:
            if (pic == self.youtube_ico or pic == self.youtube_active_ico or pic == self.my_pay_from_youtube or pic == self.order_not_found) and waiting_time == count:
                self.continue_more = False
                break


            if self.search_all_pic_screen(self.my_pay) != [] or \
                    self.search_all_pic_screen(self.no_balance) != [] or \
                    self.search_all_pic_screen(self.no_access) != [] or \
                    self.search_all_pic_screen(self.my_pay_from_youtube) != [] or \
                    self.search_all_pic_screen(self.order_not_found) != []:
                s(1.5)
                self.continue_more = False
                break

            if pic == self.perform and waiting_time == 4:
                self.continue_more = False
                break
            # if pic == self.my_pay_from_youtube or pic == self.order_not_found:
            #     pass
            waiting_time += 1
            print(f"waiting {pic} ---> {waiting_time}")
            s(time)


    def find_kudos_in_comment(self, pics):
        for  pic in pics:
            print(pic)
            matchs = self.search_all_pic_screen(pic, 0.95)
            print("before", matchs)
            s(1)
            if matchs != [] and self.next_watch:
                print("change ", matchs)
                print("count miss  ", self.count_miss)

                matchs = matchs[self.count_miss:]

            if matchs != []:
                left, top, width, _ = matchs[0]
                print("after ---> \n", "left ", left, "top", top, "width", width)
                p.moveTo(left + width + 12, top + 13)
                p.click()

                self.wait_pic(self.perform)
                if self.continue_more:
                    print("fined perform? go to click")
                    self.moveToLink(self.perform, -5, 3)
                    p.click()
                    s(0.1)
                    p.click()
                    s(0.1)
                    p.click()
                    s(0.3)
                    p.move(15, 55, 0.3)
                    # no_access

                print("continue_more ", self.continue_more)
                if self.continue_more:
                    print(pic)
                    p.move(30, 15, 1.5)
                    if pic == "picYoutube.png":
                        self.check_ico([self.youtube_active_ico, self.youtube_ico], count=1)
                        if self.continue_more:
                            p.click()
                            while self.search_all_pic_screen(self.end_movie) != []:
                                if self.search_all_pic_screen(self.timer) != []:
                                    timer = self.search_all_pic_screen(self.timer)
                                    left_timer, top_timer, width_timer, height_timer = timer[0]

                                if self.search_all_pic_screen(self.no_video, 0.8) != []:
                                    print("Video not ___________________")
                                    print("close this page ___________________")
                                    self.f5()
                                    self.next_watch = True
                                    self.count_miss += 1
                                    break

                                print(self.end_movie)
                                s(2)
                            s(2)
                            self.close_page()


                    if pic == "heart_first_png.png" or pic == "squerYoutube.png":
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
                                p.click()

                self.continue_more = True
                self.f5()
                return False

        return True


    def check_ico(self, icos, count):
        while True:
            for ico in icos:
                self.wait_pic(ico, count=count)
                if self.continue_more:
                    self.moveToLink(ico)
                    break
            break



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

    def close_page(self):
        p.hotkey("ctrl", "w")








































picYoutube = "picYoutube.png"
heart_first = "heart_first_png.png"
squerYoutube = "squerYoutube.png"
pics = [squerYoutube, heart_first, picYoutube]

account_name = "account_name_avisoooooo.png"
browser_chrome = "browser_chrome.png"
browser_chrome_ico = "browser_chrome_ico.png"
avisoooooo_check_title = "./aberavel/check_title.png"
avisoooooo = BAviso(pics, browser_chrome, browser_chrome_ico, avisoooooo_check_title, account_name)

account_name = "account_name_firefo.png"
browser_firefox = "browser_firefox.png"
browser_firefox_ico = "browser_firefox_ico.png"
firefo_check_title = "check_title_firefox.png"
firefo = BAviso(pics, browser_firefox, browser_firefox_ico, firefo_check_title, account_name)

account_name = "account_name_avisoooo.png"
browser_yandex_ico = "browser_yandex_ico.png"
avisoooo_check_title = "check_title.png"
browser_yandex ="browser_yandex.png"
avisoooo = BAviso(pics, browser_yandex, browser_yandex_ico, avisoooo_check_title, account_name)

account_name = "account_name_pinkfloyd.png"
browser_chrome = "browser_chrome.png"
browser_chrome_ico = "browser_chrome_ico.png"
pinkfloyd_check_title ="check_title_pinkfloyd.png"
pinkfloyd = BAviso(pics, browser_chrome, browser_chrome_ico, pinkfloyd_check_title, account_name)


# bots = [ pinkfloyd, firefo, avisoooo, avisoooooo, ]
# bots = [ avisoooo, avisoooooo, ]
# bots = [ firefo]
# bots = [ avisoooooo]
# bots = [ avisoooo]
bots = [ pinkfloyd,]


def go(bot):
    bot_count = 0
    while True:
        if bot.find_kudos_in_comment(pics):
            # bot.f5()
            bot_count += 1
        if bot_count == 1:
            break




while True:
    for bot in bots:
        count = 0
        next_bot = False
        while True:
            count +=1
            if bot.search_all_pic_screen(bot.account_name) != []:
                break
            s(0.2)
            p.keyDown("alt")
            p.press("tab", count, 0.3)
            p.keyUp("alt")
            s(2)
            if count >= (len(bots)+2):
                next_bot = True
                break
            # p.hotkey("alt", "tab")
            bot.f5()
            s(1)
            p.hotkey("home")
        if next_bot:
            print(f"Not found {bot.account_name}")
            continue
        print(f"Jes fined bot --->{bot.account_name}")
        print(bot.browser)
        # bot.f5()
        s(3)
        go(bot)
        # next bot
    print("15 sec rest")
    s(15)