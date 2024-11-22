import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define game window dimensions
window_width = 600
window_height = 400

# Colors (RGB format)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up the display window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Game clock to control the speed
clock = pygame.time.Clock()

# Snake block size
snake_block = 10
snake_speed = 15  # Speed of the snake

# Font settings for messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    game_window.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 6, window_height / 3])

# Function to play music
def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1, 0.0)  # Loop indefinitely

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    # Play background music when the game starts
    play_music("bensound-angelsbymyside.mp3")  # Make sure this file is in the same directory as the script

    while not game_over:

        while game_close:
            game_window.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # Check for player input to quit or restart
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling
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

        # Check for boundary collision
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the snake position
        x1 += x1_change
        y1 += y1_change
        game_window.fill(blue)

        # Draw the food
        pygame.draw.rect(game_window, yellow, [foodx, foody, snake_block, snake_block])

        # Update the snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

            # Play different music when the snake eats the apple
            pygame.mixer.music.stop()  # Stop the current background music
            play_music("bensound-curiouschild.mp3")  # Make sure this file is in the same directory as the script

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
gameLoop()