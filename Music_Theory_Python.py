import pygame
import time
import threading

# Initialize pygame mixer
pygame.mixer.init()

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
    time.sleep(1)  # Adjust duration as needed

# Notes to play simultaneously
notes_to_play = ["C", "E", "G"]

# Create and start threads
threads = [threading.Thread(target=play_note, args=(note,)) for note in notes_to_play]
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()


# thread1.join()
# thread2.join()
# thread3.join()


#Input a chord, key or note
#TAKE USER INPUT 

#Which of these do you hear 
#case note - chord or key
    #chord
        #calls function of chord
    #key
        #calls function of chord
#case chord - note or key
    #note
        #calls function of chord
    #key
        #calls function of chord
#case key - note or chord
    #note
        #calls function of chord
    #chord
        #calls function of chord