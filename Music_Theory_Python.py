import pygame
import time
import threading

# Initialize pygame mixer
pygame.mixer.init()

<<<<<<< HEAD
# Load your sound files
soundC = pygame.mixer.Sound("./Notes/C_Single_Note.mp3")  # Replace with your file
soundE = pygame.mixer.Sound("./Notes/E_Single_Note.mp3")  # Replace with your file
soundG = pygame.mixer.Sound("./Notes/G_Single_Note.mp3")  # Replace with your file

# Function to play sound1
def play_soundC():
    soundC.play()
    time.sleep(1)  # Wait for the sound to finish (adjust as per sound duration)

# Function to play sound2
def play_soundE():
    soundE.play()
    time.sleep(1)  # Wait for the sound to finish (adjust as per sound duration)

# Function to play sound3
def play_soundG():
    soundG.play()
    time.sleep(1)  # Wait for the sound to finish (adjust as per sound duration)

# Create # threads to play both sounds at the same time
thread1 = threading.Thread(target=play_soundC)
thread2 = threading.Thread(target=play_soundE)
thread3 = threading.Thread(target=play_soundG)
=======
# Load sound files by using a dictionary
notes = {
    "A#_Bb": pygame.mixer.Sound("./Notes/A#_Bb_Single_Note.mp3"),
    "A": pygame.mixer.Sound("./Notes/A_Single_Note.mp3"),
    "B": pygame.mixer.Sound("./Notes/B_Single_Note.mp3"),
    "C#_Db": pygame.mixer.Sound("./Notes/C#_Db_Single_Note.mp3"),
    "C": pygame.mixer.Sound("./Notes/C_Single_Note.mp3"),
    "D#_Eb": pygame.mixer.Sound("./Notes/D#_Eb_Single_Note.mp3"),
    "D": pygame.mixer.Sound("./Notes/D_Single_Note.mp3"),
    "E": pygame.mixer.Sound("./Notes/E_Single_Note.mp3"),
    "F#_Gb": pygame.mixer.Sound("./Notes/F#_Gb_Single_Note.mp3"),
    "F": pygame.mixer.Sound("./Notes/F_Single_Note.mp3"),
    "G#_Ab": pygame.mixer.Sound("./Notes/G#_Ab_Single_Note.mp3"),
    "G": pygame.mixer.Sound("./Notes/G_Single_Note.mp3"),
}

# Function to play a note
def play_note(note):
    notes[note].play()
    print(note)
    time.sleep(.5) # Adjust duration as needed

def play_notes(notes_list):
    for note in notes_list:
        play_note(note)  # Calls the existing play_note function


>>>>>>> 1e32d94933c8f509050aa614019a74b226af9552

# Example usage:
mary_lamb = ["E", "D", "C", "D", "E", "E", "E", "D", "D", "D", "E", "G", "G"]
alphabet = ["A", "A#_Bb", "B", "C", "C#_Db", "D", "D#_Eb", "E", "F", "F#_Gb", "G", "G#_Ab"]
# play_notes(alphabet)

time.sleep(1)

#User input
#Case C E G
#put that into array
#play that array from notes to play

#inifite chords

#predefining
#C chord (major), minor

# Ask the user for a sequence of notes
print(f"Enter any of these notes")
print(f"{alphabet}")
user_input = input("Enter notes separated by spaces (e.g., C E G): ")

# Convert input into a list
notes_list = user_input.split()

# Play the notes one by one
play_notes(notes_list)


# Notes to play simultaneously
notes_to_play = notes_list

# Create and start threads
try:
    threads = [threading.Thread(target=play_note, args=(note)) for note in notes_to_play]
    for thread in threads:
        thread.start()
except:
    print("")
    
# Wait for all threads to finish
try:
    for thread in threads:
        thread.join()
except:
    print("")


# thread1.join()
# thread2.join()
# thread3.join()

#Which of these do you want to hear 
#Input a chord, key or note
#TAKE USER INPUT 

#case note - chord or key
    #chord
        #calls function of chord
    #key
        #calls function of key
#case chord - note or key
    #note
        #calls function of note
    #key
        #calls function of key
#case key - note or chord
    #note
        #calls function of note
    #chord
        #calls function of chord