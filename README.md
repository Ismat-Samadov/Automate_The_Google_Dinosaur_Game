# Automate_The_Google_Dinosaur_Game
Write Python code to play the Google Dinosaur Game.
To play the Google Dinosaur Game using Python, you can utilize the PyAutoGUI library to simulate keypresses and interact with the game. However, note that the game needs to be played in a web browser, and the browser window should be positioned correctly for the script to work. Here's an example code:

```python
import time
import pyautogui

def play_dinosaur_game():
    # Set the initial position of the dinosaur
    dinosaur_x = 100
    dinosaur_y = 235
    
    # Start the game by pressing the spacebar
    pyautogui.press('space')
    
    while True:
        # Check for obstacles by checking the color of a pixel at a certain position
        obstacle_color = pyautogui.pixel(dinosaur_x + 80, dinosaur_y - 30)
        
        # If the color indicates an obstacle, jump by pressing the spacebar
        if obstacle_color[0] < 100:
            pyautogui.press('space')
        
        # Move the dinosaur forward
        dinosaur_x += 5
        
        # Sleep for a short duration to control the speed of the game
        time.sleep(0.01)

# Run the game
play_dinosaur_game()
```

Make sure to install the required libraries, `pyautogui`, using `pip install pyautogui`, before running the script. Additionally, you need to manually position the browser window such that the dinosaur is at the correct starting position for the script to work.

Keep in mind that this script relies on screen coordinates and pixel colors, so any changes in the game's layout or visuals may affect its functionality.