import cv2
import numpy as np
import pyautogui
from ml_engine.hand_detector import HandDetector

class VirtualMouse:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector()

        self.screenW, self.screenH = pyautogui.size()
        self.frameR = 100
        self.smoothening = 7
        self.prevX, self.prevY = 0, 0

    def run(self):
        while True:
            success, img = self.cap.read()
            img = cv2.flip(img, 1)

            img = self.detector.findHands(img)
            lmList = self.detector.findPosition(img)

            if len(lmList) != 0:
                x1, y1 = lmList[8][1], lmList[8][2]   # Index finger
                x2, y2 = lmList[12][1], lmList[12][2] # Middle finger

                fingers = self.detector.fingersUp(lmList)

                # Move Mouse
                if fingers[1] == 1 and fingers[2] == 0:
                    x3 = np.interp(x1, (self.frameR, 640 - self.frameR), (0, self.screenW))
                    y3 = np.interp(y1, (self.frameR, 480 - self.frameR), (0, self.screenH))

                    currX = self.prevX + (x3 - self.prevX) / self.smoothening
                    currY = self.prevY + (y3 - self.prevY) / self.smoothening

                    pyautogui.moveTo(currX, currY)
                    self.prevX, self.prevY = currX, currY

                # Left Click
                if fingers[1] == 1 and fingers[2] == 1:
                    length = np.hypot(x2 - x1, y2 - y1)
                    if length < 40:
                        pyautogui.click()

                # Right Click
                if fingers[1] == 1 and fingers[3] == 1:
                    pyautogui.rightClick()

            cv2.imshow("Virtual Mouse", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
