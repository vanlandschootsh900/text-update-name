#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module
import random


def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_text(screen, text, x, y, font_size, color, font_name=None, bold=False, italic=False):
    if font_name:
        font=pygame.font.font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)

    font.set_bold(bold)
    font.set_italic(italic)

    text_surface = font.render(text, True, color)
    screen.blit(text_surface,(x,y)) 

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()


    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        # Add code to draw stuff (for example) below this comment

        text1= 'Shay VanLandschoot'
        font_size1 = 48
        color1 = config.BLACK
        x1, y1 = (200,250)

        text2= 'Am Web and app'
        font_size2 = 48
        color2 = config.RED
        x2, y2 = (200,320)

        text3= 'SuttonBay Online'
        font_size3 = 48
        color3 = config.PURPLE
        x3, y3 = (475,355)

        draw_text(screen, text1 ,x1 , y1, font_size1, color1)
        draw_text(screen, text2 ,x2 , y2, font_size2, color2, bold=True)
        draw_text(screen, text3 ,x3 , y3, font_size3, color3, italic=True)


        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
