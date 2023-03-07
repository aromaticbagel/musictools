import random
import pyttsx3

# Define lists of guitar techniques and practice session focus skills
techniques = ["hammer-ons", "pull-offs", "slides", "bends", "vibrato", "sweeps", "tapping", "alternate picking"]
focus_skills = ["speed", "accuracy", "rhythm", "timing", "tone", "phrasing", "creativity", "improvisation"]

# Define a list of practice session lengths in seconds
session_lengths = list(range(25, 901))

# Initialize the pyttsx3 text-to-speech engine
engine = pyttsx3.init()

# Prompt the user for input with vocal narration
engine.say("Hey, there! Welcome back to practice.")
engine.runAndWait()
user_input = input()

# Generate a random guitar technique and focus skills
technique = random.choice(techniques)
focus_skill = random.choice(focus_skills)

# Generate a random practice session length in seconds
session_length_seconds = random.choice(session_lengths)

# Convert the practice session length to minutes and seconds
session_length_minutes = session_length_seconds // 60
session_length_seconds %= 60

# Print the generated practice routine with vocal narration
engine.say(f"Today you will practice {technique}.")
engine.say(f"Your focus skill for this session will be {focus_skill}.")
engine.say(f"Your practice session will last {session_length_minutes} minutes and {session_length_seconds} seconds.")
engine.runAndWait()

