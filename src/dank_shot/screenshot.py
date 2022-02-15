import logging

from mss import mss
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class ScreenCapture:

    border_color = (106, 181, 234)

    upper_corner = (12, 175)
    lower_corner = (680, 1266)

    background_color = (222, 222, 222)

    def __init__(self):
        logging.info('Created ScreenCapture')
        self._determine_game_bounds()

    def capture_screen(self):
        with mss() as sct:
            sct.shot()
            filename = sct.shot()

        logging.info(f'Saved screenshot to: {filename}')

        image = Image.open(filename)
        data = np.asarray(image)

        # Only capturing relevant part
        data = data[:, self.upper_corner[0]:self.lower_corner[0]]
        data = data[self.upper_corner[1]:self.lower_corner[1], :]

        return data

    def _determine_game_bounds(self):
        logging.info('Determining bounds of game')
        image = self.capture_screen()

        # Determining Center
        center_x = int(image.shape[1] / 2)
        center_y = int(image.shape[0] / 2)
        logging.info(f'Image center: ({center_x}, {center_y})')

        # Storing old upper corner for offsets
        old_upper_corner = [c for c in self.upper_corner]

        # Right frame
        for px in range(0, image.shape[1]):
            if all([image[center_y][px][i] == self.background_color[i] for i in range(3)]):
                self.upper_corner = (self.upper_corner[0] + px, self.upper_corner[1])
                break
        # Top frame
        for py in range(0, image.shape[0]):
            if all([image[py][center_x][i] == self.background_color[i] for i in range(3)]):
                self.upper_corner = (self.upper_corner[0], self.upper_corner[1] + py)
                break
        # Right frame
        for px in range(image.shape[1] - 1, 0, -1):
            if all([image[center_y][px][i] == self.background_color[i] for i in range(3)]):
                self.lower_corner = (px + old_upper_corner[0], old_upper_corner[1])
                break
        # Bottom frame
        for py in range(image.shape[0] - 1, 0, -1):
            if all([image[py][center_x][i] == self.background_color[i] for i in range(3)]):
                self.lower_corner = (self.lower_corner[0], py + old_upper_corner[1])
                break
        logging.info(f'Upper corner: {self.upper_corner}')
        logging.info(f'Lower corner: {self.lower_corner}')

        self.capture_screen()
