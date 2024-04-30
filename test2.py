from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pygame
import time
from TheDice import roll_dice_animation, calculate_winnings
from TheText import draw_text
from Constants import *
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize Pygame
pygame.init()

# Set up surfaces
screen = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/play/", response_class=HTMLResponse)
async def play_game(request: Request, bet_amount: float = Form(...)):
    player_money = PLAYER_MONEY
    initial_money = PLAYER_MONEY
    play_count = 0
    dice1 = 0
    dice2 = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        if player_money >= bet_amount:
            player_money -= bet_amount
            play_count += 1
            dice1, dice2 = roll_dice_animation(screen)
            time.sleep(1)
            pygame.display.flip()
            time.sleep(1)
            player_money = calculate_winnings(dice1, dice2, player_money)
        else:
            return templates.TemplateResponse("error.html", {"request": request})

        result = abs(dice1 - dice2)
        total_profit = player_money - initial_money

        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "dice1": dice1,
                "dice2": dice2,
                "result": result,
                "player_money": player_money,
                "bet_amount": bet_amount,
                "total_profit": total_profit,
                "play_count": play_count,
            },
        )
