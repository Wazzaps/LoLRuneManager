import pywinauto
import pyautogui

button = 'left'


def execute(page):
    # Bring window to front and calculate size
    app = pywinauto.Application().connect(title_re="League of Legends", class_name="RCLIENT")
    window = app.window(title="League of Legends")
    window.set_focus()
    winsize = window.element_info.rectangle
    ratio = winsize.width() / 1280
    
    # Locate reference point
    try:
        refX, refY, _, _ = pyautogui.locateOnScreen('editbtn.png')
    except:
        try:
            refX, refY, _, _ = pyautogui.locateOnScreen('editbtn_large.png')
        except:
            raise SyntaxError('Make sure the league client is visible on screen, with the rune editor open')
    
    # Change name
    pyautogui.moveTo(refX, refY)
    pyautogui.click(button=button)
    pyautogui.moveTo(refX + ratio * 100, refY)
    pyautogui.click(button=button)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(page[0], interval=0.005)
    
    pyautogui.PAUSE = 0.08
    
    # Primary path
    pyautogui.moveTo(refX + ratio * (90 + 38 * (page[1] - 1)), refY + ratio * 90)
    pyautogui.click(button=button)
    
    # Keystone
    pyautogui.moveTo(refX + ratio * (90 + 70 * (page[2] - 1)), refY + ratio * 200)
    pyautogui.click(button=button)
    
    # Primary R1
    pyautogui.moveTo(refX + ratio * (90 + 70 * (page[3] - 1)), refY + ratio * 300)
    pyautogui.click(button=button)
    
    # Primary R2
    pyautogui.moveTo(refX + ratio * (90 + 70 * (page[4] - 1)), refY + ratio * 400)
    pyautogui.click(button=button)
    
    # Primary R3
    pyautogui.moveTo(refX + ratio * (90 + 70 * (page[5] - 1)), refY + ratio * 500)
    pyautogui.click(button=button)
    
    # Secondary path
    pyautogui.moveTo(refX + ratio * (420 + 50 * (page[6] - 1)), refY + ratio * 90)
    pyautogui.click(button=button)
    
    # Secondary R1
    if page[7] is not 0:
        pyautogui.moveTo(refX + ratio * (420 + 70 * (page[7] - 1)), refY + ratio * 170, duration=0.2)
        pyautogui.click(button=button)
    
    # Secondary R2
    if page[8] is not 0:
        pyautogui.moveTo(refX + ratio * (420 + 70 * (page[8] - 1)), refY + ratio * 270)
        pyautogui.click(button=button)
    
    # Secondary R3
    if page[9] is not 0:
        pyautogui.moveTo(refX + ratio * (420 + 70 * (page[9] - 1)), refY + ratio * 330)
        pyautogui.click(button=button)
    
    # Save
    pyautogui.moveTo(refX + ratio * 380, refY)
    pyautogui.click(button=button)
