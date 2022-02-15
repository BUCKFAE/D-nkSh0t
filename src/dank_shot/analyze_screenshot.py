import logging

import matplotlib.pyplot as plt

from src.dank_shot.util.pixel import is_same_color

ring_color_active = (148, 148, 148)
ring_color_target = (208, 83, 42)


def analyze_screenshot(screenshot):
    logging.info('Analyzing screenshot')

    for pos_y in range(screenshot.shape[0]):
        for pos_x in range(screenshot.shape[1]):
            if is_same_color(screenshot, pos_x, pos_y, ring_color_target):
                screenshot[pos_y][pos_x] = [0, 0, 255]
            if is_same_color(screenshot, pos_x, pos_y, ring_color_active):
                screenshot[pos_y][pos_x] = [0, 255, 0]

    plt.imshow(screenshot)
    plt.show()
