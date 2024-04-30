import pygame
import random
import os
import time
from TheText import *
from Constants import *

# Load dice images and resize them
dice_images = [
    pygame.transform.scale(
        pygame.image.load(os.path.join("Dice", f"{i}.png")), (DICE_SIZE, DICE_SIZE)
    )
    for i in range(1, 7)
]

def roll_dice_animation(screen):
    """Animate the rolling of two dice."""
    final_dice = [random.randint(1, 6), random.randint(1, 6)]

    frames = 50  # Number of frames for the animation
    for i in range(frames):
        # Display random frames of dice animation
        screen.fill((16, 16, 16))

        draw_text(
            screen,
            "Rolling dices ...",
            (WIDTH // 2, HEIGHT // 2 - 200),
            color=WHITE,
            font_size=40,
        )
        draw_text(
            screen,
            "Dice 1:",
            (WIDTH // 2 - DICE_SIZE - 30, HEIGHT // 2 - 100),
            color=WHITE,
        )
        draw_text(
            screen,
            "Dice 2:",
            (WIDTH // 2 + DICE_SIZE + 30, HEIGHT // 2 - 100),
            color=WHITE,
        )

        rotate_angle1 = random.randint(1, 45) * (
            random.choice([-1, 1])
        )  # Random rotation for dice 1
        rotate_angle2 = random.randint(1, 45) * (
            random.choice([-1, 1])
        )  # Random rotation for dice 2

        # Adjust animation speed and flickering speed based on frame count
        flickering_speed = (
            0.15 if i < frames / 2 else (0.2 if i < frames - 20 else 0.25)
        )
        animation_speed = 50 if i < frames / 2 else (100 if i < frames - 20 else 200)

        if i % 4 == 0:  # Flickering effect between two images
            screen.blit(
                dice_images[random.randint(0, 5)], (WIDTH, HEIGHT // 2 - DICE_SIZE + 30)
            )
            pygame.display.flip()
            time.sleep(flickering_speed)  # Flickering speed

        # Rotate and blit dice images
        if i < frames - 1:
            for j, angle in enumerate([rotate_angle1, rotate_angle2]):
                rotated_image = pygame.transform.rotate(
                    dice_images[random.randint(0, 5)], angle
                )
                screen.blit(
                    rotated_image,
                    (
                        WIDTH // 2 - DICE_SIZE - 100 + j * (2 * DICE_SIZE + 110),
                        HEIGHT // 2 - DICE_SIZE,
                    ),
                )
                if j == 0:
                    draw_text(
                        screen,
                        str(random.randint(1, 6)),
                        (
                            WIDTH // 2 - DICE_SIZE - 100 + DICE_SIZE // 2,
                            HEIGHT // 2 + DICE_SIZE,
                        ),
                        color=WHITE,
                    )
                else:
                    draw_text(
                        screen,
                        str(random.randint(1, 6)),
                        (
                            WIDTH // 2 - DICE_SIZE - 100 + (2 * DICE_SIZE + 110) + DICE_SIZE // 2,
                            HEIGHT // 2 + DICE_SIZE,
                        ),
                        color=WHITE,
                    )

        pygame.display.flip()
        pygame.time.wait(animation_speed)  # Adjust the speed of the animation dynamically

        if i == frames - 1:

            dice1 = pygame.transform.scale(dice_images[final_dice[0] - 1], (DICE_SIZE * 1.25, DICE_SIZE * 1.25))
            dice2 = pygame.transform.scale(dice_images[final_dice[1] - 1], (DICE_SIZE * 1.25, DICE_SIZE * 1.25))

            screen.blit(dice1, ( WIDTH // 2 - DICE_SIZE - 50, HEIGHT // 2 - DICE_SIZE))
            screen.blit(dice2, ( WIDTH // 2 + 50, HEIGHT // 2 - DICE_SIZE))

            draw_text(screen, str(final_dice[0]), (WIDTH // 2 - DICE_SIZE - 5, HEIGHT // 2 + DICE_SIZE), color=WHITE, font_size = 40)
            draw_text(screen, str(final_dice[1]), (WIDTH // 2 + DICE_SIZE + 15, HEIGHT // 2 + DICE_SIZE), color=WHITE, font_size = 40)


            # Flash with glow effect
            for _ in range(5):

                draw_text(
                screen,
                "CONGRATULATIONS",
                (WIDTH // 2, HEIGHT // 2 - 100),
                color=WHITE,
                font_size= 80,
                )

                
                screen.blit(dice1, ( WIDTH // 2 - DICE_SIZE - 50, HEIGHT // 2 - DICE_SIZE))
                screen.blit(dice2, ( WIDTH // 2 + 50, HEIGHT // 2 - DICE_SIZE))

                draw_text(screen, str(final_dice[0]), (WIDTH // 2 - DICE_SIZE - 5, HEIGHT // 2 + DICE_SIZE), color=WHITE, font_size = 40)
                draw_text(screen, str(final_dice[1]), (WIDTH // 2 + DICE_SIZE + 15, HEIGHT // 2 + DICE_SIZE), color=WHITE, font_size = 40)
                
                pygame.display.flip()
                time.sleep(0.3)  # Adjust flash speed
                screen.fill((16, 16, 16))
                pygame.display.flip()
                time.sleep(0.3)  # Adjust flash speed

    return final_dice

def calculate_winnings(dice1, dice2, player_money):
    """Calculate the difference between two dice rolls and update player's money."""
    difference = abs(dice1 - dice2)
    return player_money + difference