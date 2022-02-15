import logging
import pygame
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def main():
    logging.info('Starting sample scene')

    pygame.init()

    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()

    ball = ((20, 500), (20, 50))
    ball_history = []

    loop = True

    while loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        screen.fill(WHITE)

        ball_pos = ball[0]
        ball_velo = ball[1]
        logging.info(f'Current ball pos: {ball_pos}')
        logging.info(f'Current ball velocity: {ball_velo}')

        new_velo = (ball_velo[0], ball_velo[1] - 3)
        new_ball_pos = (ball_pos[0] + ball_velo[0], ball_pos[1] - ball_velo[1])
        logging.info(f'New ball pos: {new_ball_pos}')
        logging.info(f'New ball velocity: {new_velo}')

        ball = (new_ball_pos, new_velo)

        # Drawing the ball
        pygame.draw.circle(screen, RED, ball[0], 5)

        # Drawing trajectory of the ball
        ball_history += [tuple([c for c in ball_pos])]
        for history_ball in ball_history:
            pygame.draw.circle(screen, GREEN, history_ball, 5)

        pygame.display.flip()

        if ball[0][1] > 550:
            loop = False

        clock.tick(10)
    pygame.image.save(screen, "screenshot.jpg")


if __name__ == '__main__':
    main()
