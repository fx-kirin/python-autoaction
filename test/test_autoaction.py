from unittest import TestCase
from autoaction import Autoaction
from autoaction import xutils
import numpy

class TestAutoaction(TestCase):
    def test_search_template(self):
        sscv = xutils.take_screenshot()
        template = xutils.crop_image(sscv, 30, 30, 10, 10)
        auto = Autoaction()
        auto.click_image(template, 5, 5)
        auto.sleep(1)
        auto.type(["gedit", '<Enter>'])