import cv2

cv2.ocl.setUseOpenCL(False)


class ImageMatch(object):
    def __init__(self):
        # FLANN parameters
        self.orb = cv2.ORB_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.imgs = {}

    def add(self, key, ipath):
        img = cv2.imread(ipath, 0)
        kp, des = self.orb.detectAndCompute(img, None)
        if des is not None:
            self.imgs[key] = des

    def match(self, ipath):
        img = cv2.imread(ipath, 0)
        kp, des = self.orb.detectAndCompute(img, None)

        results = {}
        for k in self.imgs:
            matches = self.bf.match(des, self.imgs[k])

            if matches:
                results[k] = len(matches)

        if results:
            results = results.items()
            results.sort(key=lambda i: -i[1])
            best_result = results[0]

            return best_result[0], (results[0][1] - results[1][1]) / 50.0

        return "none", 0
