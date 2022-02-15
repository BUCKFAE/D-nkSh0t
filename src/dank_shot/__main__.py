import logging

from src.dank_shot.analyze_screenshot import analyze_screenshot
from src.dank_shot.screenshot import ScreenCapture


def main():
    logging.info('DänkS0t started!')
    screen_capture = ScreenCapture()
    screenshot = screen_capture.capture_screen()
    analyze_screenshot(screenshot)

if __name__ == '__main__':
    main()
