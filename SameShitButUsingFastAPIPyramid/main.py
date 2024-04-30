from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import pygame
import random
import time
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize Pygame
pygame.init()

# Set up constants
WIDTH = 480
HEIGHT = 800
DICE_SIZE = 75
PLAYER_MONEY = 10
BET_AMOUNT = 2.0

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
        if i == frames - 1:
            dice1 = dice_images[final_dice[0] - 1]
            dice2 = dice_images[final_dice[1] - 1]
            return final_dice, dice1, dice2


def calculate_winnings(dice1, dice2, player_money):
    """Calculate the difference between two dice rolls and update player's money."""
    difference = abs(dice1 - dice2)
    return player_money + difference


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/play/")
async def play_game(dice1: int = Form(...), dice2: int = Form(...), player_money: int = Form(...)):
    if player_money >= BET_AMOUNT:
        player_money -= BET_AMOUNT
        dice1, dice2 = roll_dice_animation()
        time.sleep(1)  # Wait for a moment before displaying the final dice
        player_money = calculate_winnings(dice1, dice2, player_money)
    return {"dice1": dice1, "dice2": dice2, "player_money": player_money}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
