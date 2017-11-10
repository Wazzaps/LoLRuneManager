import pywinauto
import pyautogui
import time
import cv2
import numpy as np
from cvpipeline import *


def execute(isinchampselect):
    # Bring window to front
    app = pywinauto.Application().connect(title_re="League of Legends", class_name="RCLIENT")
    window = app.window(title="League of Legends")
    window.set_focus()
    winpos = window.element_info.rectangle
    print(winpos.top, winpos.left, winpos.width(), winpos.height())

    # Capture screen and convert to CV mat
    screen = pyautogui.screenshot()
    open_cv_image = np.array(screen)
    open_cv_image = open_cv_image[:, :, ::-1].copy()



    #cv2.imshow('test', open_cv_image)
    #cv2.waitKey()


