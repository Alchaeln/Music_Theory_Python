import pygame
import time
import threading

# Initialize pygame mixer
pygame.mixer.init()

# Load your sound files
sound_c = pygame.mixer.Sound("./Notes/C_Single_Note.mp3")  # Replace with your file
sound_e = pygame.mixer.Sound("./Notes/E_Single_Note.mp3")  # Replace with your file
sound_g = pygame.mixer.Sound("./Notes/G_Single_Note.mp3")  # Replace with your file

# Function to play sound_c
def play_sound_c():
    sound_c.play()
    time.sleep(1)  # Wait for the sound to finish (adjust as per sound duration)

# Function to play sound_e
def play_sound_e():
    sound_e.play()
    time.sleep(1)  # Wait for the sound to finish (adjust as per sound duration)

# Function to play sound_g
def play_sound_g():
    sound_g.play()
    time.sleep(1)  # Wait for the sound to finish (adjust as per sound duration)

# Create # threads to play both sounds at the same time
thread1 = threading.Thread(target=play_sound_c)
thread2 = threading.Thread(target=play_sound_e)
thread3 = threading.Thread(target=play_sound_g)

# Start the threads
thread1.start()
thread2.start()
thread3.start()


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