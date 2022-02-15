import logging
import re
if __name__ == '__main__':
    with open('data/pixel_data.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
        logging.info(f'Data: {data}')

        posX, posY = [int(pos[2:]) for pos in re.findall('[XY]=[0-9]+', data[0])]
        logging.info(f'Coordinates: ({posX}, {posY})')

        hex_color = data[2].split(' ')[-1][1:]
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        logging.info(f'RGB: ({r}, {g}, {b})')
