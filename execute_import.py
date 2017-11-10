import pywinauto
import pyautogui


def execute(page):
    # Bring window to front
    app = pywinauto.Application().connect(title_re="League of Legends", class_name="RCLIENT")
    window = app.window(title="League of Legends")
    window.set_focus()
    
    # Locate reference point
    refX, refY, _, _ = pyautogui.locateOnScreen('editbtn.png')
    
    # Change name
    pyautogui.moveTo(refX, refY)
    pyautogui.click()
    pyautogui.moveTo(refX + 100, refY)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(page[0], interval=0.005)
    
    pyautogui.PAUSE = 0.08
    
    # Primary path
    pyautogui.moveTo(refX + 90 + 38 * (page[1] - 1), refY + 90)
    pyautogui.click()
    
    # Keystone
    pyautogui.moveTo(refX + 90 + 70 * (page[2] - 1), refY + 200)
    pyautogui.click()
    
    # Primary R1
    pyautogui.moveTo(refX + 90 + 70 * (page[3] - 1), refY + 300)
    pyautogui.click()
    
    # Primary R2
    pyautogui.moveTo(refX + 90 + 70 * (page[4] - 1), refY + 400)
    pyautogui.click()
    
    # Primary R3
    pyautogui.moveTo(refX + 90 + 70 * (page[5] - 1), refY + 500)
    pyautogui.click()
    
    # Secondary path
    pyautogui.moveTo(refX + 420 + 50 * (page[6] - 1), refY + 90)
    pyautogui.click()
    
    # Secondary R1
    if page[7] is not 0:
        pyautogui.moveTo(refX + 420 + 70 * (page[7] - 1), refY + 170, duration=0.2)
        pyautogui.click()
    
    # Secondary R2
    if page[8] is not 0:
        pyautogui.moveTo(refX + 420 + 70 * (page[8] - 1), refY + 270)
        pyautogui.click()
    
    # Secondary R3
    if page[9] is not 0:
        pyautogui.moveTo(refX + 420 + 70 * (page[9] - 1), refY + 330)
        pyautogui.click()
    
    # Save
    pyautogui.moveTo(refX + 380, refY)
    pyautogui.click()
