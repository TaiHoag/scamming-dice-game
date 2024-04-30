document.addEventListener('DOMContentLoaded', function() {
    const rollBtn = document.getElementById('roll-btn');
    const dice1Div = document.getElementById('dice1');
    const dice2Div = document.getElementById('dice2');
    const resultDiv = document.getElementById('result');
    const playerMoneyDiv = document.getElementById('player-money');
    const betAmountDiv = document.getElementById('bet-amount');
    const totalProfitDiv = document.getElementById('total-profit');
    const totalPlaysDiv = document.getElementById('total-plays');

    let playerMoney = 10.0; // Initialize player money
    const betAmount = 3.0; // Set bet amount
    let totalPlays = 0; // Initialize total plays counter

    // Display initial values
    playerMoneyDiv.textContent = `Player Money: $${playerMoney.toFixed(2)}`;
    betAmountDiv.textContent = `Bet Amount: $${betAmount.toFixed(2)}`;
    totalProfitDiv.textContent = `Total Profit: $0.00`; // Assuming total profit starts at 0
    totalPlaysDiv.textContent = `Total plays: ${totalPlays}`;

    rollBtn.addEventListener('click', function() {
        if (playerMoney < betAmount) {
            alert("Insufficient Funds!"); // Display alert for insufficient funds
            return; // Exit the function
        }

        // Placeholder for the AJAX call to Flask route
        // Once the logic is implemented, update the UI accordingly
        // For now, let's just display random results for two dice
        const dice1 = Math.floor(Math.random() * 6) + 1; // Random number between 1 and 6 for dice 1
        const dice2 = Math.floor(Math.random() * 6) + 1; // Random number between 1 and 6 for dice 2
        const result = Math.abs(dice1 - dice2); // Calculate the absolute difference between dice values
        playerMoney = playerMoney - betAmount + result; // Update player's money
        totalPlays++; // Increment total plays counter

        dice1Div.textContent = `Dice 1: ${dice1}`;
        dice2Div.textContent = `Dice 2: ${dice2}`;
        resultDiv.textContent = `Result: ${result}`;
        playerMoneyDiv.textContent = `Player Money: $${playerMoney.toFixed(2)}`; // Display player's money with two decimal places
        totalProfitDiv.textContent = `Total Profit: ${playerMoney - 10 >= 0 ? '+$' + (playerMoney - 10).toFixed(2) : '-$' + Math.abs(playerMoney - 10).toFixed(2)}`;
        // Adjusted to calculate total profit based on initial money of 10
        totalPlaysDiv.textContent = `Total plays: ${totalPlays}`; // Update total plays counter in the UI
    });
});
