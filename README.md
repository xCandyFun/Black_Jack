# Blackjack Game

This is a simple web-based implementation of the Blackjack game built with Python and Flask. The game allows a player to compete against a computer (dealer) in a classic game of Blackjack.

## Features

- Two players: A human player and the computer (dealer).
- The player can choose to hit (draw cards) or stand (keep their current cards).
- The computer plays automatically after the player stands.
- The game ends when the player busts, the computer busts, or both players finish their turns.

## Installation

Follow these steps to run the game locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/xCandyFun/Black_Jack.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Black_Jack
    ```

3. **Create a virtual environment** (optional, but recommended):
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Flask app**:
    ```bash
    flask run
    ```

    This will start the Flask development server.

7. **Open your browser** and go to `http://127.0.0.1:5000/` to play the game.

## Usage

Once the app is running, you can open your browser and go to the URL `http://127.0.0.1:5000/`. The interface will guide you through the process of playing Blackjack against the computer.

## Acknowledgments

- This project was built with Python and Flask.