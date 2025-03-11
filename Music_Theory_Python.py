import pygame
import time
import threading

# Initialize pygame mixer
pygame.mixer.init()

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