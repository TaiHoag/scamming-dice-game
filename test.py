import pygame
import random
import time
import os

# Initialize Pygame
pygame.init()

# Set up constants
WIDTH = 480
HEIGHT = 800
WHITE = (255, 255, 255)
DICE_SIZE = 75
FONT_SIZE = 32
FONT = pygame.font.Font("8514oem.fon", FONT_SIZE)  # Default font
PLAYER_MONEY = 10
BET_AMOUNT = 2.0

# Set up surfaces
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load dice images and resize them
dice_images = [
    pygame.transform.scale(
        pygame.image.load(os.path.join("Dice", f"{i}.png")), (DICE_SIZE, DICE_SIZE)
    )
    for i in range(1, 7)
]


def roll_dice_animation():
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
                        WIDTH // 2 - DICE_SIZE - 100 + j * (2 * DICE_SIZE + 130),
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
                            WIDTH // 2 - DICE_SIZE - 100 + (2 * DICE_SIZE + 130) + DICE_SIZE // 2,
                            HEIGHT // 2 + DICE_SIZE,
                        ),
                        color=WHITE,
                    )

        pygame.display.flip()
        pygame.time.wait(
            animation_speed
        )  # Adjust the speed of the animation dynamically

        if i == frames - 1:
            dice1 = dice_images[final_dice[0] - 1]
            dice2 = dice_images[final_dice[1] - 1]
            screen.blit(dice1, (WIDTH // 2 - DICE_SIZE - 100, HEIGHT // 2 - DICE_SIZE))
            screen.blit(
                dice2,
                (
                    WIDTH // 2 - DICE_SIZE - 100 + 1 * (2 * DICE_SIZE + 130),
                    HEIGHT // 2 - DICE_SIZE,
                ),
            )
            draw_text(
                screen,
                str(final_dice[0]),
                (
                    WIDTH // 2 - DICE_SIZE - 100 + DICE_SIZE // 2,
                    HEIGHT // 2 + DICE_SIZE,
                ),
                color=WHITE,
            )
            draw_text(
                screen,
                str(final_dice[1]),
                (
                    WIDTH // 2 - DICE_SIZE - 100 + (2 * DICE_SIZE + 130) + DICE_SIZE // 2,
                    HEIGHT // 2 + DICE_SIZE,
                ),
                color=WHITE,
            )

        pygame.display.flip()

    return final_dice


def calculate_winnings(dice1, dice2, player_money):
    """Calculate the difference between two dice rolls and update player's money."""
    difference = abs(dice1 - dice2)
    return player_money + difference


def draw_text(surf, text, pos, color=WHITE, font_size=FONT_SIZE):
    """Draw text on the screen."""
    font = FONT
    text_surf = font.render(str(text), True, color)
    text_rect = text_surf.get_rect(center=pos)
    surf.blit(text_surf, text_rect)


def main():
    """Main game loop."""
    player_money = PLAYER_MONEY
    initial_money = PLAYER_MONEY
    play_count = 0
    dice1 = 0
    dice2 = 0

    while True:
        screen.fill((16, 16, 16))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if player_money >= BET_AMOUNT:
                    player_money -= BET_AMOUNT
                    play_count += 1
                    # Roll dice animation
                    dice1, dice2 = roll_dice_animation()
                    # Wait for a moment before displaying the final dice
                    time.sleep(1)
                    # Display the final dice
                    screen.blit(
                        dice_images[dice1 - 1],
                        (WIDTH // 2 - DICE_SIZE - 100, HEIGHT // 2 - DICE_SIZE),
                    )
                    screen.blit(
                        dice_images[dice2 - 1],
                        (WIDTH // 2 + DICE_SIZE + 30, HEIGHT // 2 - DICE_SIZE),
                    )
                    pygame.display.flip()
                    # Wait for 2 seconds before continuing
                    time.sleep(2)
                    player_money = calculate_winnings(dice1, dice2, player_money)
                else:
                    draw_text(
                        screen,
                        "!!!You don't have enough money to play!!!",
                        (WIDTH // 2, HEIGHT // 2),
                    )
                    pygame.display.flip()
                    time.sleep(2)  # Wait for 2 seconds before continuing
                    break

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
        draw_text(
            screen, str(dice1), (WIDTH // 2 - DICE_SIZE, HEIGHT // 2), color=WHITE
        )
        draw_text(
            screen, str(dice2), (WIDTH // 2 + DICE_SIZE, HEIGHT // 2), color=WHITE
        )

        # Calculate result and display it
        result = abs(dice1 - dice2)
        draw_text(
            screen,
            f"Result: {result}",
            (WIDTH // 2, HEIGHT // 2 + DICE_SIZE + FONT_SIZE),
            color=WHITE,
        )

        draw_text(
            screen,
            f"Player Money: ${player_money}",
            (WIDTH // 2, 70),
            color=WHITE,
            font_size=40,
        )
        draw_text(screen, f"Bet Amount: ${BET_AMOUNT}", (WIDTH // 2, 120), color=WHITE)

        total_profit = player_money - initial_money
        profit_text = f"Total Profit: {'+$' if total_profit >= 0 else '-$'}{abs(total_profit)}"
        draw_text(screen, profit_text, (WIDTH // 2, 170), color=WHITE)

        draw_text(screen, f"Total plays: {play_count}", (100, 220), color=WHITE)
        draw_text(
            screen,
            "Press space to continue playing",
            (WIDTH // 2, HEIGHT // 2 + DICE_SIZE + 3 * FONT_SIZE),
            color=WHITE,
        )
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

