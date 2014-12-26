import os
import cv2
import numpy
import xutils
import time

class Autoaction(object):
    def __init__(self, image_dir=None):
        if image_dir:
            self.image_dir = image_dir
        else:
            self.image_dir = os.curdir
    
    def sleep(self, sec):
        time.sleep(sec)
    
    def get_image(self, image_path):
        return cv2.imread(image_path)
        
    def search_template(self, template_input, quality=0.9, method=cv2.TM_CCORR_NORMED):
        sscv = xutils.take_screenshot()
        
        # load image
        if isinstance(template_input, str):
            if template_input[0] == "/":
                template_path = template_input
            else:
                template_path = os.path.join(self.image_dir, template_input)
            template = cv2.imread(template_path)
        elif isinstance(template_input, numpy.ndarray):
            template = template_input
            
        return xutils.image_search(sscv, template, quality, method)
    
    def click(self, x, y):
        return xutils.click(x, y)
    
    def click_image(self, template, x, y, quality=0.9, method=cv2.TM_CCORR_NORMED):
        result = self.search_template(template, quality, method)
        if result is None:
            raise RuntimeError("Couldn't find the template.")
        
        self.click(result[0]+x, result[1]+y)
        
    def type(self, string, hold=0.1):
        xutils.typekey(string, hold)