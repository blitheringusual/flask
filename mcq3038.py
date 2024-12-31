import pygame
import random
import csv
import argparse

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 1440
HEIGHT = 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MCQ Vocabulary Pattern Recognition Flashcards")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 78, 255)
BROWN = (64, 64, 6)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (64, 64, 6)  # Color for buttons

# Font
SMALL=36
FONT_SIZE = 48
HEADING = 96

FONT = pygame.font.Font(None, FONT_SIZE)
HEADI = pygame.font.Font(None, HEADING)
SMAL = pygame.font.Font(None, SMALL)  # Smaller font for messages

# Button dimensions !dummy
BUTTON_WIDTH = 132
BUTTON_HEIGHT = 48

# press space
def handle_spacebar_press():
    """Start shuffling choices when the spacebar is pressed."""
    global shuffle_options  # Declare that we're modifying the global variable
    shuffle_options = True  # Set the shuffle_options flag to False to stop shuffling

# Load vocabulary from CSV
def load_vocabulary(filename):
    vocabulary = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Use semicolon as delimiter
        next(reader)  # Skip header row
        for row in reader:
            vocabulary.append({"word": row[0], "meaning": row[1].strip('"')})  # Remove quotes
    return vocabulary

# Function to create a mini-dataset
def create_mini_dataset(vocabulary, size):
    """Creates a random subset of the vocabulary with the specified size."""
    mini_dataset = random.sample(vocabulary, size)  # Randomly select 5, 50, 150, 200 words
    return mini_dataset

# Parse command-line arguments for dataset size and hint
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", type=int, default=200, help="The default size of dataset is 200")
parser.add_argument("--hint", type=int, default=0, help="Place your bet on one answer using cursor, tap to select, space to shuffle")
args = parser.parse_args()

# Load vocabulary from CSV
vocabulary = load_vocabulary("vocabulary.csv")

# Create a mini-dataset, this will be epic!
mini_dataset = create_mini_dataset(vocabulary, args.dataset)
random.shuffle(mini_dataset)  # Shuffle the mini-dataset for even more randomness

# Initialize score
score = 0
attemp = 0

# Function to display the word and options
def display_word_and_options(word, meaning, options):
    """Displays the word and its meaning options on the screen."""
    screen.fill(WHITE)

    # Display the word
    word_text = HEADI.render(word, True, BLACK)
    word_rect = word_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(word_text, word_rect)

    # Display the multiple choice options
    option_height = HEIGHT // 8
    option_y = HEIGHT // 2
    for i, option in enumerate(options):
        option_text = FONT.render(option, True, BROWN)
        option_rect = option_text.get_rect(center=(WIDTH // 2, option_y + i * option_height))
        screen.blit(option_text, option_rect)
		
# Function to turn click into point
def check_answer(selected_option, meaning):
    """Record every click attempts."""
    global score, attemp
    if selected_option == meaning:
        score += 1
        return True
    else:
        attemp += 1
        return False

# Game loop
current_word_index = 0
running = True
shuffle_options = False # Flag to control shuffling

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the clicked option
            mouse_x, mouse_y = pygame.mouse.get_pos()
            option_height = HEIGHT // 8
            option_y = HEIGHT // 2
            for i in range(4):
                option_rect = pygame.Rect(0, option_y + i * option_height, WIDTH, option_height)
                # Check if the mouse is within the option rectangle
                if option_rect.collidepoint(mouse_x, mouse_y):
                    selected_option = options[i]
                    # Check the answer
                    is_correct = check_answer(selected_option, mini_dataset[current_word_index]["meaning"])
                    if is_correct:
                        print("Correct!")
                        # Move to the next word
                        current_word_index = (current_word_index + 1) % len(mini_dataset)
                        if current_word_index == 0:
                            random.shuffle(mini_dataset)  # Shuffle the mini-dataset again
                    else:
                        print("Almost there!")

        # Generate multiple choice as random as possible while ensuring unique answer
        current_word = mini_dataset[current_word_index]["word"]
        correct_meaning = mini_dataset[current_word_index]["meaning"]
        options = [correct_meaning]  # Always include the correct meaning
        while len(options) < 4:
            random_meaning_index = random.randint(0, len(mini_dataset) - 1)
            random_meaning = mini_dataset[random_meaning_index]["meaning"]
            if random_meaning not in options:
                options.append(random_meaning)
        random.shuffle(options)

    # Display the word and options
    display_word_and_options(current_word, correct_meaning, options)

    # Update the display
    pygame.display.flip()

	# Function to turn points into success rate
font = pygame.font.Font(None, 48)
score_text = font.render(f"Your success rate is {100*score/(score+attemp):.1f}%", True, BROWN)
score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
screen.blit(score_text, score_rect)
pygame.display.flip()

# Wait for a short time before quitting
pygame.time.delay(3000)  # Wait for 3 seconds

# Quit Pygame
pygame.quit()
