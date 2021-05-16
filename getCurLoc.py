
#!/usr/bin/env python
 
import time
import win32api
import win32con
#from PIL import ImageGrab
 
#img1 = ImageGrab.grab((760, 440, 1160, 640))
#time.sleep(3)

def setMouseLession():
    while True:
        pos = win32api.GetCursorPos()
        print(pos[0],pos[1])
        time.sleep(1)
"""
while True:
    #img2 = ImageGrab.grab((760, 440, 1160, 640))
 
    # 小弹窗已出现，屏幕已静止不动。
    #if img1 == img2:
    	# 小弹窗中“确定”按钮的位置。
        win32api.SetCursorPos([859, 603])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    #else:
        #simg1 = img2
"""

if __name__ == "__main__":
    setMouseLession()