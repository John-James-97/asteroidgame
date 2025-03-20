# Asteroids Game

An implementation of the classic **Asteroids** arcade game, written in Python using the Pygame library.

## Features

- Player-controlled spaceship with rotation and thrust
- Asteroids of different sizes and speeds
- Shooting mechanics to destroy asteroids
- Collision detection

## Installation

Ensure you have Python installed (preferably Python 3.7 or later). Then, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/jeffe89/asteroids.git
   cd asteroids
   ```

2. Create and activate a virtual environment:

   - On Windows:
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:

   ```sh
   pip install pygame
   ```

## Running the Game

After installation, run the game with:

```sh
python main.py
```

## Controls

- **W** - Thrust forward
- **A/D** - Rotate the spaceship
- **S** - Move backward
- **Spacebar** - Fire bullets

## How to Play

1. Start the game using the command above.
2. Use **WASD** controls to navigate the spaceship.
3. Avoid colliding with asteroids.
4. Use the **Spacebar** to shoot asteroids.
5. Destroy all asteroids to survive!

## Project Structure

- **asteroid.py** - Defines the behavior and movement of individual asteroids.
- **asteroidfield.py** - Manages the collection of asteroids in the game, including spawning and updating them.
- **circleshape.py** - Contains functionality for circular collision detection and rendering.
- **constants.py** - Stores game-wide constants, such as screen dimensions and physics values.
- **main.py** - Entry point of the game, initializes the game loop and handles overall execution.
- **player.py** - Handles the spaceship's movement, rotation, and shooting mechanics.
- **requirements.txt** - Lists the dependencies required to run the game.
- **shot.py** - Defines the properties and behavior of projectiles fired by the player.

## Author

John James

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

Enjoy playing Asteroids! 🚀
