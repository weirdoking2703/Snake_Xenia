import pygame, random
from pygame.locals import *

pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CELL_SIZE = 20  # size of each snake block
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Snake Xenia")
bg = pygame.image.load("img/bg.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont("Arial", 36)


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


# Snake and food setup
snake = [(100, 100), (80, 100), (60, 100)]  # initial 3 segments
direction = "RIGHT"
food = (random.randrange(0, SCREEN_WIDTH // CELL_SIZE) * CELL_SIZE,
        random.randrange(0, SCREEN_HEIGHT // CELL_SIZE) * CELL_SIZE)

clock = pygame.time.Clock()
run = True
game_over = False

score = 0
speed = 10

while run:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    if not game_over:
        # Move snake head
        x, y = snake[0]
        if direction == "UP":
            y -= CELL_SIZE
        if direction == "DOWN":
            y += CELL_SIZE
        if direction == "LEFT":
            x -= CELL_SIZE
        if direction == "RIGHT":
            x += CELL_SIZE
        new_head = (x, y)

        # Check collisions
        if (x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT or new_head in snake):
            game_over = True
        else:
            snake.insert(0, new_head)
            # Check if food eaten
            if new_head == food:
                score += 1
                speed += 1
                food = (random.randrange(0, SCREEN_WIDTH // CELL_SIZE) * CELL_SIZE,
                        random.randrange(0, SCREEN_HEIGHT // CELL_SIZE) * CELL_SIZE)
            else:
                snake.pop()  # remove tail if no food eaten

        # Draw food
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        draw_text(f"Score: {score}", font, WHITE, SCREEN_WIDTH - 150, 20)

    else:
        draw_text("GAME OVER!", font, WHITE, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20)
        draw_text("Click Anywhere To Restart", font, WHITE, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 20)

        restart = pygame.mouse.get_pressed()[0]
        if restart==True:  # restart game
            snake = [(100, 100), (80, 100), (60, 100)]
            direction = "RIGHT"
            food = (random.randrange(0, SCREEN_WIDTH // CELL_SIZE) * CELL_SIZE,
                    random.randrange(0, SCREEN_HEIGHT // CELL_SIZE) * CELL_SIZE)
            score = 0
            speed = 10
            game_over = False

    pygame.display.update()
    clock.tick(speed)  # controls snake speed (10 FPS)

pygame.quit()
