import pyautogui as p
import subprocess as sp

from time import sleep as s

print("Start _________________________________________")


class BAviso:

    def __init__(self):
        left, top, width, heigth = 0, 0, 800, 420
        party_screenshoot_1 = p.screenshot(region=(left, top, width, heigth))
        party_screenshoot_1.save("party_screenshoot_1.png")

        left, top, width, heigth = 800, 0, 800, 420
        party_screenshoot_2 = p.screenshot(region=(left, top, width, heigth))
        party_screenshoot_2.save("party_screenshoot_2.png")

        left, top, width, heigth = 0, 440, 800, 420
        party_screenshoot_3 = p.screenshot(region=(left, top, width, heigth))
        party_screenshoot_3.save("party_screenshoot_3.png")

        left, top, width, heigth = 800, 440, 800, 420
        party_screenshoot_4 = p.screenshot(region=(left, top, width, heigth))
        party_screenshoot_4.save("party_screenshoot_4.png")


    def update_screenshoot(self, left, top, width, heigth, png):
        party_screenshoot = p.screenshot(region=(left, top, width, heigth))
        party_screenshoot.save(png)

    def search_pic_in_box_screen(self, pic, confidence=0.9):
        return [match for match in p.locateAllOnScreen(pic, confidence=confidence)]

    def f5(self, x=600, y=500, time=0.3):
        p.moveTo(x, y, time)
        p.hotkey("f5")

    def close_page(self):
        p.hotkey("ctrl", "w")

aviso = BAviso()

# check firefo
firefo = "party_screenshoot_1.png"

while True:
    # search squerYoutube
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    squerYoutube = list(p.locateAll("heart_first_png.png", firefo, confidence=0.9))
    if squerYoutube != []:
        print("fined ico ", squerYoutube)
        # move to locate element
        print("move to locate heart_first_png ", squerYoutube)
        p.moveTo(squerYoutube[0][0] + squerYoutube[0][2] + 10, squerYoutube[0][1] + 10, 0.5)
        print("click ...", squerYoutube)
        p.click()
        s(0.5)
        p.click()

    # search heart_first_png
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    heart_first_png = list(p.locateAll("heart_first_png.png", firefo, confidence=0.9))
    if heart_first_png != []:
        print("fined ico ", heart_first_png)
        # move to locate element
        print("move to locate heart_first_png ", heart_first_png)
        p.moveTo(heart_first_png[0][0] + heart_first_png[0][2] + 10, heart_first_png[0][1] + 10, 0.5)
        print("click ...", heart_first_png)
        p.click()
        s(0.5)
        p.click()

    # search picYoutube
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    picYoutube = list(p.locateAll("picYoutube.png", firefo, confidence=0.9))
    if picYoutube != []:
        print("fined ico ", picYoutube)
        # move to locate element
        print("move to locate picYoutube ", picYoutube)
        p.moveTo(picYoutube[0][0]+ picYoutube[0][2]+10 , picYoutube[0][1]+10, 0.5)
        print("click ...", picYoutube)
        p.click()
        s(0.5)
        p.click()

    # search my_pay
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    pay = list(p.locateAll("my_pay.png", firefo, confidence=0.7))
    if  pay != []:
        # yet have pay
        print("yet have pay, move for click")
        p.moveTo(pay[0][0], pay[0][1], 0.3)
        p.click()
        print("reload page ...")
        # reload page
        aviso.f5()
        break


    # search order_not_found no_access no_balance no_pay
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    for pic in ["order_not_found.png", "no_access.png", "no_balance.png", "no_pay.png"]:
        order_not_found = list(p.locateAll(pic, firefo, confidence=0.7))
        if order_not_found != []:
            # yet have pay
            print("order_not_found", pic)
            p.moveTo(order_not_found[0][0], order_not_found[0][1], 0.3)
            p.click()
            print("reload page ...")
            # reload page
            aviso.f5()
            break

    # search perform
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    perform = list(p.locateAll("perform.png", firefo, confidence=0.7))
    if perform != []:
        print("perform move to and click ")
        p.moveTo(perform[0][1] + 4, perform[0][1] + 4, 0.3)
        p.click()


    # search play youtube
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    youtube_play_red_ico = list(p.locateAll("youtube_play_red_ico.png", firefo, confidence=0.8))
    if youtube_play_red_ico != []:
        print("youtube_play move and click ", youtube_play_red_ico)
        p.moveTo(youtube_play_red_ico[0][0], youtube_play_red_ico[0][1], 0.4)
        p.click()
    youtube_play_dark_ico = list(p.locateAll("youtube_play_dark_ico.png", firefo, confidence=0.8))
    if youtube_play_dark_ico != []:
        print("youtube_play move and click ", youtube_play_dark_ico)
        p.moveTo(youtube_play_dark_ico[0][0], youtube_play_dark_ico[0][1], 0.4)
        p.click()

    # search timer
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 420, "party_screenshoot_1.png")
    timer = list(p.locateAll("timer.png", firefo, confidence=0.70))
    if timer != []:
        print("fined timer ")

    # search play minimal ico
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 430, "party_screenshoot_1.png")
    play_minmal_ico = list(p.locateAll("play_minimal_ico.png", firefo, confidence=0.8))
    if play_minmal_ico != []:
        print("youtube minimal play move and click ",  play_minmal_ico)
        p.moveTo(play_minmal_ico[0][0]+5,  play_minmal_ico[0][1]+5, 0.4)
        p.click()

    # search youtube lable youtube_lable_ico.png",
    #                 "no_video.png",
    #                 "no_video_2.png",
    #                 "my_pay_from_youtube.png"
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 430, "party_screenshoot_1.png")
    for pic in ["youtube_lable_ico.png",
                "no_video.png",
                "no_video_2.png",
                "my_pay_from_youtube.png"]:
        youtube_lable_ico = list(p.locateAll(pic, firefo, confidence=0.8))
        if youtube_lable_ico != []:
            print("youtube_lable_ico fined, close page",  pic)
            p.moveTo(youtube_lable_ico[0][0], youtube_lable_ico[0][1], 0.4)
            p.click()
            aviso.close_page()
            break

    # search check
    # update firefo
    aviso.update_screenshoot(0, 0, 800, 430, "party_screenshoot_1.png")
    check = list(p.locateAll("check.png", firefo, confidence=0.8))
    if check != []:
        print("youtube minimal play move and click ", check)
        p.moveTo(check[0][0] + 5, check[0][1] + 5, 0.4)
        p.click()
        s(3)
        p.click()


    # pause loop
    print("pause loop 5 sec...")
    s(5)

# if __main__ == "__main__":
#     aviso = BAviso()

