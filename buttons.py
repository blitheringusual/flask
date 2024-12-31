import pygame

# Assuming you've already defined the necessary constants (WIDTH, HEIGHT, BLUE, SMALL_FONT, BLACK)
# from your previous code.
WIDTH = 800
HEIGHT = 600
# Button dimensions
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

# Create the "Stop" button
stop_button_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - 20, HEIGHT - BUTTON_HEIGHT - 20, BUTTON_WIDTH, BUTTON_HEIGHT)

# Function to draw buttons
def draw_button(text, x, y, width, height, color, font):
    """Draws a button on the screen."""
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=((x + width // 2), (y + height // 2)))
    screen.blit(text_surface, text_rect)

def handle_button_click(button_rect, mouse_x, mouse_y)

	return
	button_rect.collidepoint(mouse_x, mouse_y)
# Button definitions (for easier management)

def stop_shuffling()

	global shuffle_options
	shuffle_oprions = False
buttons = [
    {"text": "Previous", "x": 20, "y": HEIGHT - button_height - 20, "width": button_width, "height": button_height, "action": lambda:  # Use a lambda function for the action
        update_current_word_index("previous")},
    {"text": "Next", "x": WIDTH // 2 - button_width // 2, "y": HEIGHT - button_height - 20, "width": button_width, "height": button_height, "action": lambda:
        update_current_word_index("next")},
    {"text": "Submit", "x": WIDTH - button_width - 20, "y": HEIGHT - button_height - 20, "width": button_width, "height": button_height, "action": lambda:
        set_game_started(False)}  # Use a helper function
]

# Helper function to update current_word_index
def update_current_word_index(direction):
    global current_word_index
    if direction == "previous":
        current_word_index = (current_word_index - 1) % len(mini_dataset)
        if current_word_index == 0:
            random.shuffle(mini_dataset)  # Shuffle the mini-dataset again
    elif direction == "next":
        current_word_index = (current_word_index + 1) % len(mini_dataset)
        if current_word_index == 0:
            random.shuffle(mini_dataset)  # Shuffle the mini-dataset again

# Helper function to set game_started
def set_game_started(value):
    global game_started
    game_started = value

