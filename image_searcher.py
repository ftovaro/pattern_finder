print('Starting')

from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import cv2

# time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# click(187, 2123)


# Find wheat to harvest


# scenario_img = cv2.imread('3.jpg', cv2.IMREAD_UNCHANGED)
# wheat_img = cv2.imread('base.jpg', cv2.IMREAD_UNCHANGED)

scenario_img = cv2.imread('scenario1.png', cv2.IMREAD_UNCHANGED)
wheat_img = cv2.imread('wheat1.png', cv2.IMREAD_UNCHANGED)

# cv2.imshow('Map', scenario_img)
# cv2.waitKey()

# cv2.imshow('Product', wheat_img)
# cv2.waitKey()

result = cv2.matchTemplate(scenario_img, wheat_img, cv2.TM_CCOEFF_NORMED)
# cv2.imshow('Result', result)
# cv2.waitKey()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = wheat_img.shape[1]
h = wheat_img.shape[0]

cv2.rectangle(scenario_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (255, 255, 0), 2)

cv2.imshow('Map', scenario_img)
cv2.waitKey()

threshold = .50

yloc, xloc = np.where(result >= threshold)

print(len(xloc))


for (x, y) in zip(xloc, yloc):
    cv2.rectangle(scenario_img, (x, y), (x + w, y + h), (255, 255, 0), 2)

# cv2.imshow('Map', scenario_img)
# cv2.waitKey()

# A Rectangle is:
# x, y, w, h
rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

print(len(rectangles))

rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

print(len(rectangles))

for(x, y, w, h) in rectangles:
    cv2.rectangle(scenario_img, (x, y), (x + w, y + h), (255, 255, 0), 2)


cv2.imshow('Map', scenario_img)
cv2.waitKey()

# Left click to open menu in a random position inside the rectangle

# for (x, y, w, h) in rectangles:
#     # Calculate a random position within the rectangle
#     rand_x = random.randint(x, x + w)
#     rand_y = random.randint(y, y + h)

#     # Click at the random position
#     click(rand_x, rand_y)
#     time.sleep(0.5)  # Add a small delay to simulate human interaction
#     break


# Left click to select Reap

print('Closing program')
