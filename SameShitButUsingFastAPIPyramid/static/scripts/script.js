document.addEventListener("DOMContentLoaded", () => {
    const playBtn = document.getElementById("play-btn");
    const dice1Img = document.getElementById("dice1");
    const dice2Img = document.getElementById("dice2");
    const resultMsg = document.getElementById("result");
    const playerMoney = document.getElementById("player-money");
    const betAmount = document.getElementById("bet-amount");
    const totalProfit = document.getElementById("total-profit");
    const totalPlays = document.getElementById("total-plays");

    async function playGame() {
        const response = await fetch("/play/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
                dice1: Math.floor(Math.random() * 6) + 1,
                dice2: Math.floor(Math.random() * 6) + 1,
                player_money: parseInt(playerMoney.textContent.split("$")[1]),
            }),
        });
        const data = await response.json();
        dice1Img.src = `/static/images/${data.dice1}.png`;
        dice2Img.src = `/static/images/${data.dice2}.png`;
        playerMoney.textContent = `Player Money: $${data.player_money}`;
        if (data.dice1 === data.dice2) {
            resultMsg.textContent = "It's a tie!";
        } else {
            resultMsg.textContent = `Result: ${Math.abs(data.dice1 - data.dice2)}`;
        }
    }

    playBtn.addEventListener("click", playGame);
});
