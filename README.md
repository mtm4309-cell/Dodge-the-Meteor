## DODGE THE METOR  [February 2024 - April 2024] ##

An arcade-style 2D game built using the Pygame Module in Python. This project served as a stepping stone to immerse myself in the world of Game Development, where I learned about event handling, game loops, and basic collision detection.


## Technical Functions ##

 --> **Collision Physics:** Setting up the hitboxes of the player and the oncoming meteors; Detecting the collisions between the player vector and the oncoming projectiles.  
 --> **Score and Fail State Logic:** Tracking the duration of the player surviving, and triggering an immediate game-over state once the collision between the player and the meteor occurs.  
 --> **Procedural Entity Generation:** Forming falling meteor objects at randomised X-Axis Coordinates, mimicking downward gravitational acceleration.  

## How to Download & Play

### Prerequisites
Make sure you have **Python 3.x** installed on your system. You can download it from [python.org](https://www.python.org/).

### Step-by-Step Instructions

1. **Download the Game:**
   - Click the green **Code** button at the top right of this repository page.
   - Select **Download ZIP**.
   - Extract the downloaded `.zip` file to a folder on your computer.

2. **Install Required Packages:**
   - Open your Terminal / Command Prompt inside the extracted folder.
   - Run the following command to install PyGame:
     ```bash
     pip install pygame
     ```

3. **Launch the Game:**
   - In the same terminal window, run:
     ```bash
     python main.py
     ```
     *(If your main script uses a different name, replace `main.py` with your file name, e.g., `dodge_meteor.py`)*

---

 ## Controls ##

 --> **Move Right:** Right Arrow Key Or the 'D' Button  
 --> **Move Left:** Left Arrow Key or the 'A' Button  
