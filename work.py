import pygame
import random

# Initialize pygame
pygame.init()

# Set up game window dimensions
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Music")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up the snake speed and clock
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Font for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

from moviepy.editor import VideoFileClip

def video_to_audio(video_file, audio_file):
    # Load the video file
    video = VideoFileClip(video_file)

    # Extract the audio from the video
    audio = video.audio

    # Write the audio to an mp3 file
    audio.write_audiofile(audio_file)

    # Close the audio and video objects to free up resources
    audio.close()
    video.close()

# Example usage:
video_file = "your_video.mp4"  # Replace with your video file
audio_file = "output_audio.mp3"  # Output audio file name
video_to_audio(video_file, audio_file)

# Music and Sound Effects setup (use dictionary)
music_dict = {
    "background": "background_music.mp3",  # Replace with your background music file
    "eat": "eat_sound.wav",                # Sound for eating food
    "game_over": "game_over_sound.wav",    # Sound for game over
}

# Load music files into the dictionary
try:
    pygame.mixer.music.load(music_dict["background"])  # Background music
    pygame.mixer.music.set_volume(0.5)  # Adjust volume (0.0 to 1.0)
    eat_sound = pygame.mixer.Sound(music_dict["eat"])  # Eat sound effect
    game_over_sound = pygame.mixer.Sound(music_dict["game_over"])  # Game over sound effect
except pygame.error:
    print("Music or sound effect file not found!")

# Function to display the score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    window.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Generate food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    pygame.mixer.music.play(-1, 0.0)  # Start playing background music in a loop

    while not game_over:

        while game_close:
            window.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # Play the game over sound effect
            pygame.mixer.Sound.play(game_over_sound)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
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
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

            # Play the eating sound effect
            pygame.mixer.Sound.play(eat_sound)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()