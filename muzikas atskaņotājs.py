import pygame
pygame.init()

# --------------------------mūzikas mape
mixer.music.load("file='D:\Dziesmas\Arzemju\Best Of 2004\2004-009 Ciara Featuring Petey Pablo - Goodies.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("Spiest 'p' lai pauzētu")
    print("Spiest 'a' lai atsāktu")
    print("Spiest 's' lai regulētu skaļumu")
    print("Spiest 'i' lai izietu")

    ch = input("['p','a','s','i']>>>")

    if ch == "p":
        mixer.music.pause()
    elif ch == "a":
        mixer.music.unpause()
    elif ch == "s":
        v = float(input("Skaļums(0 to 1): "))
        mixer.music.set_volume(v)
    elif ch == "i":
        mixer.music.stop()
        break
