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
