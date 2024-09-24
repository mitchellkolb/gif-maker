import random
from guiFile import start_gui

random_text_list = [
    "Hello, World!",
    "Welcome to PyGObject!",
    "Random Text Here",
    "Enjoy coding in Python!",
    "Linux Mint is awesome!"
]

def get_random_text():
    """Return a random text from the list."""
    return random.choice(random_text_list)

if __name__ == "__main__":
    # Pass the random text function to the GUI and start it
    start_gui(get_random_text)  # Use start_gui from guiFile

