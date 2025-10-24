import time
import threading
import pygame

mp3_file = "back_to_friends.mp3" 


lyrics = [
    ("",2),
    ("How can we go back to being friends", 3),
    ("When we just shared a bed?", 2.8),
    ("How can you look at me and pretend", 4),
    ("I'm someoe yove never met?", 0),
    ("",5),
    ("It was last December",3),
    ("You were layin' on my chest",4),
    ("I still remember",2.5),
    ("I was scared to take a breath, didn't want you to move your head",4),
    ("",0),
    ("How can we go back to being friends", 2.3),
    ("When we just shared a bed? (Yeah)", 3),
    ("How can you look at me and pretend", 4),
    ("I'm someoe yove never met?", 0),
    ("",0),


]


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

def display_lyrics():
    for line, delay in lyrics:
        line_to_print = "\t" + line
        for char in line_to_print:
            print(char, end='', flush=True)
            time.sleep(0.05)  
        print()  
        time.sleep(delay)  


if __name__ == "__main__":
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

    display_lyrics()

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)
