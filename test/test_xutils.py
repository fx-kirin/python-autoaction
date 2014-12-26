from unittest import TestCase
from autoaction import xutils
import numpy
import cv2
from matplotlib import pyplot as plt

class TestXutils(TestCase):
    def test_screenshot(self):
        sscv = xutils.take_screenshot()
        self.assert_(isinstance(sscv, numpy.ndarray), "take_screenshot returns wrong instance.")
        plt.imshow(cv2.cvtColor(sscv, cv2.COLOR_BGR2RGB))
        plt.show()
        
    def test_crop_image(self):
        sscv = xutils.take_screenshot()
        cropped = xutils.crop_image(sscv, 10, 30, 20, 30)
        plt.imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
        plt.show()
        
    def test_image_search(self):
        sscv = xutils.take_screenshot()
        for i in range(10):
            cropped = xutils.crop_image(sscv, 10*i, 30*i, 90, 90)
            match = xutils.image_search(sscv, cropped)
            self.assertEqual((10*i, 30*i), match, "match point was wrong. (%d, %d) != (%d, %d)"%(10*i, 30*i, match[0], match[1]))
        