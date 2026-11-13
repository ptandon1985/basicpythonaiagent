from datetime import datetime
import random
import secrets
import string

def get_current_time():
    """Returns Current time """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def roll_dice():
    """Simulates rolling a six-sided dice and returns the result."""
    return random.randint(1, 6)

def generate_password(length=12):
    """Generates a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += secrets.choice(characters)
    return password