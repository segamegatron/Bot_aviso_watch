from time import sleep as s
import pyautogui as p
pic = "account_name_avisoooo.png"
pic = "picYoutube.png"

while True:
    party_screenshoot = p.screenshot(region=(0,
                       440,
                         800,
                         440))
    party_screenshoot.save("party_screenshoot_3.png")
    elements_in_where_pic = list(p.locateAll("corona.png", "party_screenshoot_3.png", confidence=0.8))
    # mathcs = [match for match in p.locateAllOnScreen("squerYoutube.png", confidence=0.8)] # "check_title_pinkfloyd.png")] pinkfloyd_sek.png
    # print("Jes match --> ", mathcs)
    # p.moveTo(mathcs[0][0], mathcs[0][1], 1)
    print(elements_in_where_pic)
    s(3)

# test = p.locateOnScreen(pic, confidence=0.8)
# test = p.locate(pic, pic, confidence=0.8)
# test = p.l(pic, confidence=0.8)
# test = p.moveTo(p.size()[0]- 10, p.size()[1] - 10, 3)
# test = p.locateCenterOnScreen(pic)
# test = p.onScreen(, 1)
# p.alert("sdvsdvs")
# p.confirm("sdvsdvs")
# test = p.prompt("sdvsdvs")
# p.moveTo(100, 100, 4, p.easeInQuad)
# p.moveTo(1000, 800, 4, p.easeOutQuad)
# p.moveTo(100, 80, 4, p.easeOutBounce)
# p.write('Hello world!', interval=0.25)
# im1 = p.screenshot()
#
# left, top, width, heigth = 0, 0, 800, 420
# im2 = p.screenshot(region=(left, top, width, heigth))
# im2.save("party_screenshoot_1.png")
#
# left, top, width, heigth = 800, 0, 800, 420
# im2 = p.screenshot(region=(left, top, width, heigth))
# im2.save("party_screenshoot_2.png")
#
# left, top, width, heigth = 0,440, 800, 420
# im2 = p.screenshot(region=(left, top, width, heigth))
# im2.save("party_screenshoot_3.png")
#
# left, top, width, heigth = 800,440, 800, 420
# im2 = p.screenshot(region=(left, top, width, heigth))
# im2.save("party_screenshoot_4.png")
#
#
# print(p.size())
# while True:
#     print(p.position())
#

# print(test)