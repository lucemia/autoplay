import os
from os.path import basename
from .match import ImageMatch
from .models import ScreenShot
from django.core.files import File
import time

matcher = ImageMatch()


def load_status_imgs(folder):
    for ipath in os.listdir(folder):
        if ipath.endswith('.png'):
            matcher.add(basename(ipath).split('.')[0], folder + '/' + ipath)


def check_status(img):
    return matcher.match(img)


def tab(x, y):
    print 'tab', x, y
    os.system("adb shell input tap %s %s" % (x, y))


def screenshot():
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")

    screenshot = ScreenShot()
    screenshot.file.save('screenshot.png', File(open('screen.png')))
    screenshot.save()

    return screenshot


def trust_master():
    while True:
        screenshot()

        status, confidence = check_status('screen.png')
        print status, confidence
        if confidence and confidence > 0.7:
            if status == "maze":
                tab(300, 500)
            elif status == "reward":
                tab(300, 900)
            elif status == "friend":
                tab(200, 350)
            elif status == "confirm":
                tab(300, 900)
            elif status == "battle":
                tab(80, 920)
            elif status == "result":
                tab(300, 900)
            elif status == "exp":
                tab(300, 500)
            elif status == "items":
                tab(300, 900)
        else:
            time.sleep(1)


load_status_imgs('./screenshot/status')

trust_master()
