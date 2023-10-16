import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Tamaño de la ventana
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Tamaño de los bloques de la serpiente y de la fruta
BLOCK_SIZE = 20

# Velocidad de la serpiente
SNAKE_SPEED = 15

# Crear la ventana del juego
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Función para reiniciar el juego
def reset_game():
    global snake, direction, score, game_over
    snake = [(100, 50)]
    direction = "RIGHT"
    score = 0
    game_over = False

# Función para dibujar la serpiente
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# Función principal del juego
def main():
    global direction, snake, score, game_over

    reset_game()

    # Inicialización de la posición de la fruta
    fruit_x = random.randrange(1, (WINDOW_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE
    fruit_y = random.randrange(1, (WINDOW_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Capturar las teclas presionadas para cambiar la dirección de la serpiente
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        if not game_over:
            # Mover la serpiente
            if direction == "UP":
                new_head = (snake[0][0], snake[0][1] - BLOCK_SIZE)
            if direction == "DOWN":
                new_head = (snake[0][0], snake[0][1] + BLOCK_SIZE)
            if direction == "LEFT":
                new_head = (snake[0][0] - BLOCK_SIZE, snake[0][1])
            if direction == "RIGHT":
                new_head = (snake[0][0] + BLOCK_SIZE, snake[0][1])

            # Verificar colisiones
            if new_head[0] == fruit_x and new_head[1] == fruit_y:
                snake.append(new_head)
                score += 10
                fruit_x = random.randrange(1, (WINDOW_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE
                fruit_y = random.randrange(1, (WINDOW_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
            else:
                snake.pop()

            # Verificar colisiones con los bordes
            if (
                new_head[0] >= WINDOW_WIDTH
                or new_head[0] < 0
                or new_head[1] >= WINDOW_HEIGHT
                or new_head[1] < 0
                or new_head in snake[1:]
            ):
                game_over = True

            snake.insert(0, new_head)

            # Dibujar la ventana del juego
            game_window.fill(BLACK)
            draw_snake(snake)
            pygame.draw.rect(game_window, WHITE, pygame.Rect(fruit_x, fruit_y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.display.flip()

            # Controlar la velocidad del juego
            pygame.time.Clock().tick(SNAKE_SPEED)
        else:
            # Mostrar el puntaje y esperar a que se presione Enter para reiniciar
            font = pygame.font.Font(None, 36)
            text = font.render("Puntaje: " + str(score), True, WHITE)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            game_window.blit(text, text_rect)
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

if __name__ == "__main__":
    main()