import pygame
import sys
import time
import random

snake_speed = 11

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
orange = pygame.Color(255, 128, 0)
gray = pygame.Color(128, 128, 128)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snakes Game by Kubi')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()


def reset_game():
    # Restablece todas las variables del juego a sus valores iniciales
    global snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score, game_over, run
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    game_over = False # Declarar game_over como global
    run = True # Reestablecer la variable run para continuar el juego

# Función para dibujar la serpiente

# Función principal del juego
def main():
    global snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score, game_over, run
    
    reset_game() # Llamar a la función para iniciar el juego
    

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]

    # fruit position
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # displaying Score function
    def show_score(choice, color, font, size):

        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)

        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)

        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()

        # displaying text
        game_window.blit(score_surface, score_rect)

    # game over function
    def game_over():

        game_window.fill(blue)
        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)

        # Create the text surface for the "YOU LOSE" message.
        you_lose_surface = my_font.render(
            'YOU LOSE', True, white)

        # Create the text surface for the "Press "enter" to restart the game" message.
        restart_surface = my_font.render(
            'Press "enter" to restart the game.', True, green)

        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()

        # create a rectangular object for the text
        # surface object
        game_over_rect2 = you_lose_surface.get_rect()
        
        # create a rectangular object for the text
        # surface object
        game_over_rect3 = restart_surface.get_rect()

        # setting position of the text
        game_over_rect.midtop = (window_x / 2, window_y / 4)

        # setting position of the text
        game_over_rect2.midtop = (window_x / 2, window_y / 8)
        
        # setting position of the text
        game_over_rect3.midtop = (window_x / 2, window_y / 2)

        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # Blit the "YOU LOSE" surface to the game over surface.
        game_window.blit(you_lose_surface, game_over_rect2)
        pygame.display.flip()
                
        # Blit the "YOU LOSE" surface to the game over surface.
        game_window.blit(restart_surface, game_over_rect3)
        pygame.display.flip()

       
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    reset_game()
                    waiting = False

            # after 2 seconds we will quit the program
            #time.sleep(5)

            # deactivating pygame library
            #pygame.quit()

            # quit the program
            #quit()

 
    # Main Function

    # setting default while
    # true
    while run:

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            # Capturar las teclas presionadas para cambiar la dirección de la serpiente    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(gray)

        for pos in snake_body:
            pygame.draw.rect(game_window, orange,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, green, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()

        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
        

        # Close Window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Reiniciar el juego cuando se presione la tecla "R"
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        #    reset_game()


        # displaying score continuously
        show_score(1, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)


if __name__ == "__main__":
    main()