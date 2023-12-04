import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)

# Display
dis_width = 300  # 1/4 of original width
dis_height = 300  # 1/4 of original height
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Xenzia')

# Clock
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 5  # Reduced snake speed

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    score = 0  # Initialize score

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Allow snake to emerge from the opposite border
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width - snake_block
        elif y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height - snake_block

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)  # Changed background color to black

        # Draw food (white)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_over = True

        # Draw snake (red) with a wavy pattern
        for i, segment in enumerate(snake_List):
            if i % 2 == 0:
                pygame.draw.rect(dis, red, [segment[0], segment[1], snake_block, snake_block])
            else:
                pygame.draw.rect(dis, white, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1  # Increment score when food is eaten

        clock.tick(snake_speed)

    message("Your Score: " + str(score), white)  # Display score after game ends
    pygame.display.update()
    time.sleep(2)  # Display score for 2 seconds before quitting

    pygame.quit()
    quit()

gameLoop()
