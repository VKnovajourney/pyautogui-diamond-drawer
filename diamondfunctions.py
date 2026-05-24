import pyautogui
import random
import time

# ==============================
# SETTINGS
# ==============================

pyautogui.FAILSAFE = True

START_DELAY = 5
DRAW_SPEED = 0.05
CLICK_SPEED = 0.01

INITIAL_SIZE = 100
SIZE_DECREASE = 6

TOTAL_LAYERS = 20
VERTICAL_SHIFT = 6

COLOR_Y = 103
COLOR_POSITIONS = [
    984, 1014, 1044, 1074,
    1104, 1134, 1164, 1194,
    1224, 1254, 1284
]


# ==============================
# SETUP FUNCTIONS
# ==============================

def select_pencil_tool():
    """
    Select the MS Paint pencil tool.
    """
    pyautogui.moveTo(317, 103, duration=CLICK_SPEED)
    pyautogui.click()


def wait_for_paint():
    """
    Give user time to open MS Paint.
    """
    print("You have 5 seconds to open MS Paint...")
    time.sleep(START_DELAY)


def get_starting_position():
    """
    Allow user to choose starting position.
    """
    pyautogui.alert(
        text='Move mouse to TOP vertex position, then press OK',
        title='Diamond Drawer',
        button='OK'
    )

    time.sleep(2)

    return pyautogui.position()


# ==============================
# COLOR FUNCTIONS
# ==============================

def select_color(color_x):
    """
    Select a specific color from palette.
    """
    pyautogui.click(
        color_x,
        COLOR_Y,
        duration=CLICK_SPEED
    )


def select_random_color():
    """
    Select random color from palette.
    """
    color_x = random.choice(COLOR_POSITIONS)

    select_color(color_x)


# ==============================
# DRAWING FUNCTIONS
# ==============================

def draw_diamond(x, y, size):
    """
    Draw one diamond layer.
    """

    # Focus canvas
    pyautogui.click(x, y, duration=CLICK_SPEED)

    # Move to start
    pyautogui.moveTo(x, y)

    # Draw edges
    pyautogui.dragRel(size, size, duration=DRAW_SPEED)

    pyautogui.dragRel(-size, size, duration=DRAW_SPEED)

    pyautogui.dragRel(-size, -size, duration=DRAW_SPEED)

    pyautogui.dragRel(size, -size, duration=DRAW_SPEED)
