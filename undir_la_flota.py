import pygame

import const
from text_input import TextInput


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Undir la Flota')
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(const.Color.WHITE)

    while not game_ended:
        # events.event_listener({})

        text_input.read()
        text, rect = text_input.get_text(0, 0)
        screen.blit(text, rect)

        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)


game_ended = False
text_input = TextInput()


if __name__ == '__main__':
    main()
