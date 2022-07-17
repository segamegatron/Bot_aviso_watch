import pyautogui as p
import subprocess as sp

from time import sleep as s

print("Start _________________________________________")


# print("wait 15 мин")
# s(15*60)
class BAviso:

    def __init__(self, accuant):
        self.accuant = accuant

    def update_screenshoot(self):
        party_screenshoot = p.screenshot(region=(self.accuant["left"],
                                                 self.accuant["top"],
                                                 self.accuant["width"],
                                                 self.accuant["heigth"]))
        party_screenshoot.save(self.accuant["screenshoot"])

    def search_pic_in_box_screen(self, pic, confidence=0.9):
        return [match for match in p.locateAllOnScreen(pic, confidence=confidence)]

    def f5(self):
        p.hotkey("f5")

    def close_page(self):
        p.hotkey("ctrl", "w")

    def goToURL(self, url="https://aviso.bz/work-youtube"):
        p.hotkey("ctrl", "l")
        s(0.2)
        #p.hotkey("ctrl", "a")
        p.write(url, 0.1)
        p.hotkey("ENTER")

    def update_area(self, what_search_pic, where_pic, confidence=0.8):
        aviso.update_screenshoot()
        elements_in_where_pic = list(p.locateAll(what_search_pic, where_pic, confidence))
        return elements_in_where_pic

# 1 firefo
left, top, width, heigth = 0, 0, 800, 420
size_screen = {"width": 1600, "height": 900}
firefo = {"check_title": "check_title_firefox.png",
          "screenshoot": "party_screenshoot_1.png",
          "left": left,
          "top": top,
          "width": width,
          "heigth": heigth,
          "screen_x": 0,
          "screen_y": 0,
          "heart_and_squer": False,
          "title_earn": "title_earn_firefo.png",
          "urls": {"serfing": "https://aviso.bz/work-serf", "youtube": "https://aviso.bz/work-youtube",},
          }

# 2 avisoooooo
left, top, width, heigth = 800, 0, 800, 420
avisoooooo = {"check_title": "check_title_avisoooooo.png",
              "screenshoot": "party_screenshoot_2.png",
              "left": left,
              "top": top,
              "width": width,
              "heigth": heigth,
              "screen_x": 800,
              "screen_y": 0,
              "heart_and_squer": False,
              "title_earn": "title_earn_avisoooooo.png",
              "urls": {"serfing": "https://aviso.bz/work-serf", "youtube": "https://aviso.bz/work-youtube",},
              }

# 3 avisoooo
left, top, width, heigth = 0, 440, 800, 420
avisoooo = {"check_title": "check_title_avisoooo.png",
            "screenshoot": "party_screenshoot_3.png",
            "left": left,
            "top": top,
            "width": width,
            "heigth": heigth,
            "screen_x": 0,
            "screen_y": 440,
            "heart_and_squer": False,
            "title_earn": "title_earn_avisoooo.png",
            "urls": {"serfing": "https://aviso.bz/work-serf", "youtube": "https://aviso.bz/work-youtube",},

            }

# 4 pinkfloyd
left, top, width, heigth = 800, 440, 800, 420
pinkfloyd = {"check_title": "check_title_pinkfloyd.png",
             "screenshoot": "party_screenshoot_4.png",
             "left": left,
             "top": top,
             "width": width,
             "heigth": heigth,
             "screen_x": 800,
             "screen_y": 440,
             "heart_and_squer": False,
             "title_earn": "title_earn_pinkfloyd.png",
             "urls": {"serfing": "https://aviso.bz/work-serf", "youtube": "https://aviso.bz/work-youtube",},
             }

url_serfing = "https://aviso.bz/work-serf"
url_youtube = "https://aviso.bz/work-youtube"
count = 0
while True:
    for accuant in [avisoooooo, firefo, pinkfloyd, avisoooo]:
        # search squerYoutube
        aviso = BAviso(accuant)
        print(accuant)

        # move to center accuante
        p.moveTo(accuant["left"] + accuant["width"] / 2, accuant["top"] + accuant["heigth"] / 2 + 40, 0.5)

        # search check
        # update
        aviso.update_screenshoot()
        check = list(p.locateAll("check.png", accuant["screenshoot"], confidence=0.8))
        if check != []:
            print("youtube minimal play move and click ", check)
            p.moveTo(accuant["screen_x"] + check[0][0] + 5, accuant["screen_y"] + check[0][1] + 5, 0.4)
            p.click()
            s(3)
            p.click()
            continue

        # # search perform_check
        # # update
        # aviso.update_screenshoot()
        # perform_check = list(p.locateAll("perform_and_check.png", accuant["screenshoot"], confidence=0.9))
        # if perform_check != []:
        #     check_in_perform_and_check = list(p.locateAll("perform_and_check.png", accuant["screenshoot"], confidence=0.7))
        #     print("search perform_check move to and click ")
        #     x = accuant["screen_x"] + check_in_perform_and_check[0][1] + perform_check[0][2]
        #     y = accuant["screen_y"] + check_in_perform_and_check[0][1] + 4
        #     print(x, y)
        #     p.moveTo(x, y, 0.3)
        #     p.click()
        #     s(3)
        #     p.click()

        # search perform
        # update firefo
        aviso.update_screenshoot()
        perform = list(p.locateAll("perform.png", accuant["screenshoot"], confidence=0.7))
        if perform != []:
            print("perform move to and click ")
            x = accuant["screen_x"] + perform[0][1] + 4
            y = accuant["screen_y"] + perform[0][1] + 4
            print(x, y)
            p.moveTo(x, y, 0.3)
            p.click()
            # continue

        # search my_pay
        # update firefo
        aviso.update_screenshoot()
        pay = list(p.locateAll("my_pay.png", accuant["screenshoot"], confidence=0.7))
        if pay != []:
            # yet have pay
            print("yet have pay, move for click")
            p.moveTo(accuant["screen_x"] + pay[0][0], accuant["screen_y"] + pay[0][1], 0.3)
            p.click()
            print("reload page ...")
            # reload page
            aviso.f5()

            # continue

        # update
        aviso.update_screenshoot()
        squerYoutube = list(p.locateAll("squerYoutube.png", accuant["screenshoot"], confidence=0.9))
        if squerYoutube != []:
            accuant["heart_and_squer"] = True
            print("fined ico ", squerYoutube)
            # move to locate element
            print("move to locate squerYoutube ", squerYoutube)
            p.moveTo(accuant["screen_x"] + squerYoutube[0][0] + squerYoutube[0][2] + 13,
                     accuant["screen_y"] + squerYoutube[0][1] + 10, 0.5)
            print("click ...", squerYoutube)
            p.click()
            s(0.5)
            p.click()
            # continue

        # search heart_first_png
        # update
        aviso.update_screenshoot()
        heart_first_png = list(p.locateAll("heart_first_png.png", accuant["screenshoot"], confidence=0.9))
        if heart_first_png != []:
            accuant["heart_and_squer"] = True
            print("fined ico ", heart_first_png)
            # move to locate element
            print("move to locate heart_first_png ", heart_first_png)
            p.moveTo(accuant["screen_x"] + heart_first_png[0][0] + heart_first_png[0][2] + 10,
                     accuant["screen_y"] + heart_first_png[0][1] + 10, 0.5)
            print("click ...", heart_first_png)
            p.click()
            s(0.5)
            p.click()
            # continue

        # search picYoutube
        # update firefo
        aviso.update_screenshoot()
        picYoutube = list(p.locateAll("picYoutube.png", accuant["screenshoot"], confidence=0.9))
        if picYoutube != []:
            print("fined ico ", picYoutube)
            # move to locate element
            print("move to locate picYoutube ", picYoutube)
            p.moveTo(accuant["screen_x"] + picYoutube[0][0] + picYoutube[0][2] + 15,
                     accuant["screen_y"] + picYoutube[0][1] + 10, 0.5)
            print("click ...", picYoutube)
            p.click()
            s(0.5)
            p.click()

        # search order_not_found no_access no_balance no_pay
        # update firefo
        aviso.update_screenshoot()
        for pic in ["order_not_found.png", "no_access.png", "no_balance.png", "no_pay.png", ]:
            order_not_found = list(p.locateAll(pic, accuant["screenshoot"], confidence=0.8))
            if order_not_found != []:
                # yet have pay
                print("order_not_found", pic)
                p.moveTo(accuant["screen_x"] + order_not_found[0][0], accuant["screen_y"] + order_not_found[0][1], 0.3)
                p.click()
                print("reload page ...")
                # reload page
                aviso.f5()
                break
                # continue

        # search play youtube
        # update firefo
        aviso.update_screenshoot()
        youtube_play_red_ico = list(p.locateAll("youtube_play_red_ico.png", accuant["screenshoot"], confidence=0.8))
        if youtube_play_red_ico != []:
            print("youtube_play move and click ", youtube_play_red_ico)
            p.moveTo(accuant["screen_x"] + youtube_play_red_ico[0][0], accuant["screen_y"] + youtube_play_red_ico[0][1],
                     0.4)
            p.click()
            continue
        youtube_play_dark_ico = list(p.locateAll("youtube_play_dark_ico.png", accuant["screenshoot"], confidence=0.8))
        if youtube_play_dark_ico != []:
            print("youtube_play move and click ", youtube_play_dark_ico)
            p.moveTo(accuant["screen_x"] + youtube_play_dark_ico[0][0],
                     accuant["screen_y"] + youtube_play_dark_ico[0][1], 0.4)
            p.click()
            continue

        # search timer
        # update firefo
        aviso.update_screenshoot()
        timer = list(p.locateAll("timer.png", accuant["screenshoot"], confidence=0.70))
        if timer != []:
            print("fined timer ")

        # search play minimal ico
        # update firefo
        aviso.update_screenshoot()
        play_minimal_ico = list(p.locateAll("play_minimal_ico.png", accuant["screenshoot"], confidence=0.8))
        if play_minimal_ico != []:
            print("youtube minimal play move and click ", play_minimal_ico)
            p.moveTo(accuant["screen_x"] + play_minimal_ico[0][0] + 5, accuant["screen_y"] + play_minimal_ico[0][1] + 5,
                     0.4)
            p.click()
            continue

        # search          "no_video.png",
        #                 "no_video_2.png",
        #                 "my_pay_from_youtube.png"
        # update firefo
        aviso.update_screenshoot()
        for pic in [
            "no_video.png",
            "no_video_2.png",
            "my_pay_from_youtube.png",
            "no_video_3.png", ]:
            no_video = list(p.locateAll(pic, accuant["screenshoot"], confidence=0.8))
            if no_video != []:
                print("youtube_lable_ico fined, close page", pic)
                p.moveTo(accuant["screen_x"] + no_video[0][0], accuant["screen_y"] + no_video[0][1], 0.4)
                p.click()
                aviso.close_page()
                s(0.2)
                aviso.f5()
                break

        # search youtube_lable_ico.png
        # update firefo
        aviso.update_screenshoot()
        youtube_lable_ico = list(p.locateAll("youtube_lable_ico.png", accuant["screenshoot"], confidence=0.8))
        if youtube_lable_ico != []:
            # search title_earn
            aviso.update_screenshoot()
            title_earn = list(p.locateAll(accuant["title_earn"], accuant["screenshoot"], confidence=0.8))
            if title_earn != []:
                p.moveTo(accuant["screen_x"] + youtube_lable_ico[0][0],
                         accuant["screen_y"] + youtube_lable_ico[0][1], 0.1)
                p.click()
                print("CLOSE PAGE")
                aviso.close_page()
            # search check_title
            aviso.update_screenshoot()
            check_title = list(p.locateAll(accuant["check_title"], accuant["screenshoot"], confidence=0.8))
            if check_title != []:
                print("check_title find ", accuant["screen_x"])
                print("search check_title fined, close page", accuant["check_title"])
                p.moveTo(accuant["screen_x"] + youtube_lable_ico[0][0],
                         accuant["screen_y"] + youtube_lable_ico[0][1], 0.4)
                p.click()
                aviso.close_page()

        # search check_title
        # aviso.update_screenshoot()
        # check_title = list(p.locateAll(accuant["check_title"], accuant["screenshoot"], confidence=0.8))
        # if check_title != []:
        #     print("search check_title fined, close page", accuant["check_title"])
        #     p.moveTo(accuant["screen_x"] + check_title[0][0] + check_title[0][2]+170, accuant["screen_y"] + check_title[0][1], 0.4)
        #     p.click()
        #     s(0.2)
        # aviso.close_page()

        # youtube_pause
        aviso.update_screenshoot()
        youtube_pause = list(p.locateAll("youtube_pause.png", accuant["screenshoot"], confidence=0.8))
        if youtube_pause != []:
            print("youtube_pause move and click ", accuant["screen_x"])
            p.moveTo(accuant["screen_x"] + youtube_pause[0][0] + 5, accuant["screen_y"] + youtube_pause[0][1] + 5, 0.4)
            s(0.1)
            p.click()
            s(0.1)
            aviso.close_page()
            s(0.1)
            aviso.f5()

        # allow_watch
        aviso.update_screenshoot()
        allow_watch = list(p.locateAll("allow_watch.png", accuant["screenshoot"], confidence=0.8))
        if allow_watch != []:
            print("youtube_pause move and click ", accuant["screen_x"])
            p.moveTo(accuant["screen_x"] + allow_watch[0][0] + 15, accuant["screen_y"] + allow_watch[0][1] + 15, 0.7)
            s(0.1)
            p.click()
            # s(0.1)
            # # aviso.close_page()
            # s(0.1)
            # aviso.f5()

        # page_youtube_check_title
        aviso.update_screenshoot()
        page_youtube_check_title = list(
            p.locateAll("page_youtube_check_title.png", accuant["screenshoot"], confidence=0.8))
        if page_youtube_check_title != []:
            print("page_youtube_check_title find ", accuant["screen_x"])
            # search check_title
            aviso.update_screenshoot()
            check_title = list(p.locateAll(accuant["check_title"], accuant["screenshoot"], confidence=0.8))
            if check_title != []:
                print("search check_title fined, close page", accuant["check_title"])
                p.moveTo(accuant["screen_x"] + page_youtube_check_title[0][0] + 15,
                         accuant["screen_y"] + page_youtube_check_title[0][1] + 15, 0.7)
                p.click()
                s(0.1)
                aviso.close_page()

        # search "no_task.png"
        aviso.update_screenshoot()
        no_task = list(
            p.locateAll("no_task.png", accuant["screenshoot"], confidence=0.8))
        if no_task != []:
            print("search no_task fined, go to serf", no_task)
            p.moveTo(accuant["screen_x"] + no_task[0][0],
                     accuant["screen_y"] + no_task[0][1], 0.2)
            p.click()
            s(0.1)
            # redirect
            accuant["status"] = "serf"
            print(accuant)
            aviso.goToURL(accuant["urls"]["serfing"])
            s(3)
            # scroll gorizontal
            p.vscroll(210)
            # search element serfing
            while accuant["status"] == "serf":
                print("update page")
                corona = aviso.update_area("corona.png", accuant["screenshoot"])
                if corona == []:
                    # scroll vertical
                    print("scrolling 50")
                    p.scroll(-50)
                    s(1)
                    continue
                if corona != []:
                    p.moveTo(accuant["screen_x"] + corona[0][0] + corona[0][2] + 15,
                             accuant["screen_y"] + corona[0][1] + 10, 0.5)
                    p.click

            # search element


        # # pause loop
        if count == 300:
            print("pause loop 60 sec...")
            s(60)
            count = 0
        count += 1
        print("remaning before pause --->", count)
        #
        # print("pause loop 5 sec...")
        # s(5)

# if __main__ == "__main__":
#     aviso = BAviso()





















