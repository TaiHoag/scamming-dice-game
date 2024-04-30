import pygame
import time
from TheDice import roll_dice_animation, calculate_winnings
from TheText import draw_text
from Constants import WIDTH, HEIGHT, WHITE, DICE_SIZE, FONT_SIZE, PLAYER_MONEY, BET_AMOUNT


# Initialize Pygame
pygame.init()

# Set up surfaces
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def main():
    """Main game loop."""
    player_money = PLAYER_MONEY
    initial_money = PLAYER_MONEY
    play_count = 0
    dice1 = 0
    dice2 = 0

    # Coordinates and size of the ROLL button
    roll_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + DICE_SIZE + 3 * FONT_SIZE, 100, 50)

    while True:
        screen.fill((16, 16, 16))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the mouse click is within the ROLL button
                if roll_button_rect.collidepoint(event.pos):
                    if player_money >= BET_AMOUNT:
                        player_money -= BET_AMOUNT
                        play_count += 1
                        # Roll dice animation
                        dice1, dice2 = roll_dice_animation(screen)
                        # Wait for a moment before displaying the final dice
                        time.sleep(1)
                        # Display the final dice
                        pygame.display.flip()
                        # Wait for 2 seconds before continuing
                        time.sleep(1)
                        player_money = calculate_winnings(dice1, dice2, player_money)
                    else:
                        draw_text(
                            screen,
                            "!!!You don't have enough money to play!!!",
                            (WIDTH // 2, HEIGHT // 2),
                        )
                        pygame.display.flip()
                        time.sleep(2)  # Wait for 2 seconds before continuing

        # Draw the ROLL button
        pygame.draw.rect(screen, WHITE, roll_button_rect)
        draw_text(screen, "ROLL", roll_button_rect.center, color=(0, 0, 0), font_size=24)

        # Draw other text and elements
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

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
