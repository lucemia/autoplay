import os
from os.path import basename
from .match import ImageMatch
from .models import ScreenShot, OrbMatcher, ImageHash
from django.core.files import File
import time
import requests
import imagehash
from PIL import Image

matcher = ImageMatch()


def load_status_imgs(folder):
    for ipath in os.listdir(folder):
        if ipath.endswith('.png'):
            matcher.add(basename(ipath).split('.')[0], folder + '/' + ipath)


def compute_hash(screenshot):
    try:
        ImageHash.objects.get(screenshot=screenshot)
    except ImageHash.DoesNotExist:
        with open('temp.png', 'wb') as ofile:
            screenshot.file.open()
            ofile.write(screenshot.file.read())
            screenshot.file.close()

        image = Image.open('temp.png')
        ahash = imagehash.average_hash(image)
        phash = imagehash.phash(image)
        dhash = imagehash.dhash(image)
        whash = imagehash.whash(image)

        hash, _ = ImageHash.objects.update_or_create(
            screenshot=screenshot,
            defaults={
                'ahash': ahash,
                'phash': phash,
                'dhash': dhash,
                'whash': whash
            }
        )


def check_status(screenshot):
    try:
        OrbMatcher.objects.get(screenshot=screenshot)
    except OrbMatcher.DoesNotExist:
        with open('temp.png', 'wb') as ofile:
            ofile.write(screenshot.file.read())
            screenshot.file.close()

        status, confidence = matcher.match("temp.png")

        match, _ = OrbMatcher.objects.update_or_create(
            screenshot=screenshot,
            defaults={
                "status": status,
                "confidence": confidence
            }
        )
        return match


def tap(x, y):
    os.system("adb shell input tap %s %s" % (x, y))


def swipe(x1, y1, x2, y2):
    os.system("adb shell input swipe %s %s %s %s" % (x1, y1, x2, y2))


def screenshot():
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")

    screenshot = ScreenShot()
    screenshot.file.save('screenshot.png', File(open('screen.png')))
    screenshot.save()

    return screenshot


def scan():
    for screenshot in ScreenShot.objects.all():
        try:
            check_status(screenshot)
            compute_hash(screenshot)
        except:
            print screenshot, 'failed'
            # pass


def trust_master():
    while True:
        screen_shot = screenshot()

        match = check_status(screen_shot)

        status, confidence = match.status, match.confidence
        print status, confidence
        if status == "friend" and confidence >= 0.3:
            confidence = 0.4

        if confidence and confidence >= 0.4:
            if status == "maze":
                tap(300, 500)
            elif status == "reward":
                tap(300, 900)
            elif status == "friend":
                tap(200, 350)
            elif status == "confirm":
                tap(300, 900)
            elif status == "battle":
                tap(80, 920)
            elif status == "result":
                tap(300, 900)
            elif status == "exp":
                tap(300, 500)
            elif status == "items":
                tap(300, 900)
            elif status == "no_en" and confidence > 0.6:
                tap(180, 570)
                time.sleep(10)
            elif status in ("connect_error", "connect_error1"):
                tap(300, 550)

        else:
            time.sleep(1)
