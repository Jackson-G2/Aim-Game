import random
import pygame
import time
pygame.init()

from pygame import MOUSEBUTTONDOWN
from pygame.gfxdraw import circle

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aim Trianer")

font = pygame.font.Font(None, 36)
missed_font = pygame.font.Font(None, 26)
missed_message = missed_font.render("Missed", True, (255, 50, 50))

circles = [
    [400, 300],
    [200, 250],
    [600, 200]
]

missed = 0
circle_radius = 50
score = 0

start_time = time.time() # this gets the current time
duration = 10
missed_time = 0

# Store the last missed click postion
last_miss_x, last_miss_y = None, None

running = True
while running and time.time() - start_time < duration:
    screen.fill((10, 0, 10))  # Black ish Background

    #draw circles
    for circle in circles:
        pygame.draw.circle(screen, (150, 175, 255), (circle[0], circle[1]), circle_radius)

    # draw score
    score_text = font.render(f"Score: {score}", True,(20, 255, 20)) # Green
    screen.blit(score_text, (20, 20))

    if last_miss_x is not None and time.time() - missed_time < 1:
        missed_message = missed_font.render("Missed!", True, (255, 50, 50))
        screen.blit(missed_message, (last_miss_x, last_miss_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect a click
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for circle in circles:
                distance = ((mouse_x - circle[0]) ** 2 + (mouse_y - circle[1]) ** 2) ** 0.5
                if distance <= circle_radius: # Clicked inside circle
                    circle[0] = random.randint(30, 770) # Move to New Random y
                    circle[1] = random.randint(30, 570) # Move to New Random y
                    score += 1
                    print("New Score!", score)
                    break # stop checking for other circles if one is hit

            else: # if no circle was clicked, its a miss
                missed += 1
                score -= 1
                last_miss_x, last_miss_y = mouse_x, mouse_y # Save missed click location
                missed_time = time.time() # save the time of the miss
                print(f"Missed! {score}")

    pygame.display.flip()

pygame.quit()