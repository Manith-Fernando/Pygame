# This code is a basic template for creating a Pygame window and setting up a game loop.
import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the window
width = 800
height = 600

# Create the Pygame window
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Set the window title
pygame.display.set_caption("Game Window")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Custom event for toggle fullscreen
toggle_fullscreen_event = pygame.USEREVENT + 1

# Game loop
running = True
fullscreen = False
while running:
    # Handle events
    for event in pygame.event.get():
        if (
            event.type != pygame.QUIT
            and event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
            or event.type == pygame.QUIT
        ):
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            # Toggle fullscreen on 'f' key press
            if fullscreen:
                pygame.display.set_modePython/Pygame/Game Window Template.py((width, height), pygame.RESIZABLE)
            else:
                pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.FULLSCREEN)
            fullscreen = not fullscreen
        elif event.type != pygame.KEYDOWN and event.type == pygame.VIDEORESIZE:
            # Handle window resize event
            width, height = event.size
            window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # Game logic goes here

    # Clear the window
    window.fill((0, 0, 0))

    # Draw game objects here

    # Update the window display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()