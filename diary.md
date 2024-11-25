
# ChatGPT Coding Diary

## Project Name: _[Insert project name]_

### Date: _[11/25/24]_

---

## 1. **Task/Problem Description**

Briefly describe the problem you're trying to solve or the task you're working on.

Example:
> I need to write a program that has the UI of the snake game that plays music and chnages everytime the snake eats something.

---

## 2. **Initial Approach/Code**

Describe the initial approach you took to solving the problem. If you started writing code, include it here.

import pydub

# import pygame
# import random
# import time

# # Initialize pygame
# pygame.init()

- What was your plan for solving the problem?
Ask chatgpt how to code what i want to code, but in steps
- Did you have any initial thoughts or strategies before using ChatGPT?
I had the idea of what I wanted to do, but no idea on how to execute it.

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. 
Also include what code from ChatGPT you are unsure of and craft a question that asks for further clarification. 

How to make snake game in python
How to import music in python
How to make a music file
can you change my code so that when the snake eats the food, music that is imported is selected randomly

## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.

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

# Function to randomly select a music file from a list
def random_music():
    music_list = [
        "bensound-angelsbymyside.mp3",  # Make sure the files exist
        "bensound-curiouschild.mp3",
        "bensound-creativeminds.mp3"
    ]
    return random.choice(music_list)

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

    # Play random background music when the game starts
    play_music(random_music())  # Play random music at the beginning

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
                        return  # Restart the game

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

            # Play a random music track when the snake eats the food
            pygame.mixer.music.stop()  # Stop the current music
            play_music(random_music())  # Play random music

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
gameLoop()


- What was ChatGPT's solution or suggestion?
It basically told me what i needed to do to get the result i want 
- How did it differ from your original approach?
 I had no original approach because I wasn't sure how to code it 
---

## 5. **Reflection on Changes**

Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:

- Why do you think ChatGPT's suggestions are helpful or relevant?
It offers a different approach and suggestions on how to code something.
- Did the suggestions improve your code? How?
Yes because after adding the suggestions, my code worked
- Did you understand why the changes were made, or are you still uncertain about some parts?
Yes, except for the UI part. I understand if i want msuic to be randomly chosen from my imported music, I need a list

Example:
> ChatGPT recommended using a more efficient sorting algorithm like quicksort. I think this will improve the runtime for large inputs, but I need to review the algorithm's complexity to fully understand its advantages.

---

## 6. **Testing and Results**

After making the changes, did you test your code? What were the results?
My code was sucessful

- Did you run any tests (e.g., unit tests, edge cases)?
Yes, whether the music worked or not
- Did the code work as expected after incorporating ChatGPT's changes?
Yes

```python
# Example: Testing the updated sorting function
numbers = [5, 2, 9, 1]
print(optimized_sort(numbers))  # Expected output: [1, 2, 5, 9]
```

- Did you encounter any bugs or issues during testing?
The music wouldn't stop playing but that was because I had it playing from the website.
---

## 7. **What Did You Learn?**

In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 

Example:
> I learned how to make snake game with music that changes everytime the snake eats and the usaage of the list

---