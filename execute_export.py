import pywinauto
import pyautogui
import numpy as np
import os
import subprocess
from cvpipeline import *


def execute(isinchampselect):
    # Bring window to front
    app = pywinauto.Application().connect(title_re="League of Legends", class_name="RCLIENT")
    window = app.window(title="League of Legends")
    window.set_focus()
    winpos = window.element_info.rectangle

    # Get resources
    pathmask = cv2.imread("pathmask.png", cv2.IMREAD_GRAYSCALE)
    runemask = cv2.imread("runemask.png", cv2.IMREAD_GRAYSCALE)

    # Capture screen and convert to CV mat
    screen = pyautogui.screenshot()
    open_cv_image = np.array(screen)
    open_cv_image = open_cv_image[:, :, ::-1]
    open_cv_image = open_cv_image[winpos.top:winpos.top+winpos.height(), winpos.left:winpos.left+winpos.width()]

    # Process image
    pipeline = CVPipeline()
    pipeline.process(open_cv_image, pathmask, runemask)
    path1 = cv2.boundingRect(pipeline.find_contours_0_output[0])
    path2 = cv2.boundingRect(pipeline.find_contours_0_output[1])

    if path1[0] > path2[0]:
        path1, path2 = path2, path1

    paths = 1 + round((path1[0] - 99) / 40), 1 + round((path2[0] - 429) / 50)

    runes = [cv2.boundingRect(x) for x in pipeline.filter_contours_output]
    runes = [(x[0], x[1]) for x in runes]
    primaryrunes = [1 + round((x[0] - 121) / 66) for x in runes if x[0] < 300][::-1]
    secondaryrunes_ = [(1 + round((x[0] - 446) / 66), round((x[1] - 278) / 78)) for x in runes if x[0] > 300][::-1]
    secondaryrunes = [0, 0, 0]
    for i in secondaryrunes_:
        secondaryrunes[i[1]] = i[0]

    path = os.path.join(os.environ['USERPROFILE'], 'Documents/My Runes.txt')
    with open(path, "a+") as myfile:
        myfile.write('Type Name Here::' + ','.join([str(x) for x in ([paths[0]] + primaryrunes + [paths[1]] + secondaryrunes)]) + '\r\n')
    subprocess.Popen(['notepad', path])


